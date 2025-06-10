import os
from flask import Flask, request, jsonify
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image # Importar Pillow diretamente para algumas operações

app = Flask(__name__)

# --- 1. Carregar o Modelo ---
# O modelo_cifar10.h5 está na pasta superior (seu_projeto_cnn/)
# Então, precisamos subir um nível para encontrá-lo.
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'modelo_cifar10.h5')

try:
    model = tf.keras.models.load_model(MODEL_PATH)
    # Opcional: Imprimir um resumo do modelo para confirmar que carregou
    model.summary()
    print(f"Modelo carregado com sucesso de: {MODEL_PATH}")
except Exception as e:
    print(f"Erro ao carregar o modelo: {e}")
    print(f"Verifique se o arquivo do modelo existe em: {MODEL_PATH}")
    # Se o modelo não carregar, a API pode não funcionar corretamente.
    # Considerar sair ou levantar um erro fatal aqui em um ambiente de produção.
    exit() # Sair do aplicativo se o modelo não puder ser carregado

# --- 2. Definir as classes do CIFAR-10 ---
CLASS_NAMES = [
    "avião", "automóvel", "pássaro", "gato", "cervo",
    "cachorro", "sapo", "cavalo", "navio", "caminhão"
]

# --- 3. Endpoint da API para Previsão ---
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Nome do arquivo inválido'}), 400

    if file:
        try:
            # Carregar a imagem com Pillow para garantir a compatibilidade
            img = Image.open(file.stream).convert('RGB') # Garante 3 canais de cor

            # Redimensionar para 32x32 pixels, que é o tamanho de entrada do CIFAR-10
            img = img.resize((32, 32), Image.LANCZOS) # Use Image.LANCZOS para melhor qualidade de redimensionamento

            # Converter para array NumPy
            img_array = image.img_to_array(img)

            # Expandir as dimensões para criar um batch de tamanho 1 (batch_size, height, width, channels)
            img_array = np.expand_dims(img_array, axis=0)

            # Normalizar os pixels (assumindo que seu modelo foi treinado com pixels normalizados para 0-1)
            img_array = img_array / 255.0

            # Fazer a previsão
            predictions = model.predict(img_array)
            # Obter a classe com maior probabilidade
            predicted_class_index = np.argmax(predictions[0])
            predicted_class_name = CLASS_NAMES[predicted_class_index]
            confidence = float(np.max(predictions[0])) # Convertendo para float nativo do Python

            return jsonify({
                'prediction': predicted_class_name,
                'confidence': confidence,
                'all_probabilities': predictions[0].tolist() # Opcional: mostrar todas as probabilidades
            })

        except Exception as e:
            # Captura erros de processamento de imagem ou previsão
            return jsonify({'error': f'Erro ao processar imagem ou fazer previsão: {str(e)}'}), 500

    return jsonify({'error': 'Ocorreu um erro inesperado.'}), 500

# --- 4. Rodar a Aplicação Flask ---
if __name__ == '__main__':
    # Use host='0.0.0.0' para que a API seja acessível de outras máquinas na rede local
    # debug=True para desenvolvimento (recarga automática), defina como False para produção
    app.run(debug=True, host='0.0.0.0', port=5000)