import requests
import os

# Certifique-se de que a imagem de teste está neste caminho.
# O caminho abaixo assume que 'aviao.jpg' está na mesma pasta do script 'test_api_troubleshoot.py'
IMAGE_PATH = 'aviao.jpg'

if not os.path.exists(IMAGE_PATH):
    print(f"Erro: Imagem de teste não encontrada em '{IMAGE_PATH}'. Por favor, verifique o caminho.")
    exit()

api_url = "http://localhost:5000/predict"

try:
    with open(IMAGE_PATH, 'rb') as f:
        # 'file' é o nome do campo que a API espera no request.files
        # ('nome_do_arquivo', conteúdo_do_arquivo, 'tipo_mime')
        files = {'file': (os.path.basename(IMAGE_PATH), f.read(), 'image/jpeg')} 
        
        response = requests.post(api_url, files=files)

    if response.status_code == 200:
        print("Previsão da API (resposta bem-sucedida):")
        print(response.json())
    else:
        print(f"Erro na requisição (Status Code: {response.status_code}):")
        print(response.text) # Isso vai mostrar a mensagem de erro da API (ex: "Nenhum arquivo enviado")

except requests.exceptions.ConnectionError:
    print("Erro de Conexão: A API Flask não está rodando ou o endereço está incorreto.")
    print("Certifique-se de que 'python app.py' está sendo executado no terminal.")
except Exception as e:
    print(f"Um erro inesperado ocorreu: {e}")