# Projeto de Classificação de Imagens CIFAR-10 com CNNs e API REST

Este repositório contém um projeto completo de Visão Computacional focado na classificação de imagens do dataset CIFAR-10 utilizando Redes Neurais Convolucionais (CNNs). O projeto abrange desde a análise de dados e treinamento do modelo até a simulação em ambiente de produção através de uma API REST.

## 🌟 Visão Geral do Projeto

O objetivo principal deste trabalho é demonstrar o ciclo de vida de um modelo de Machine Learning em Visão Computacional:

1.  **Exploração de Dados:** Entendimento do dataset CIFAR-10.
2.  **Pré-processamento:** Preparação e aumento de dados (Data Augmentation).
3.  **Modelagem e Treinamento:** Construção e treinamento de uma CNN do zero.
4.  **Avaliação:** Análise do desempenho do modelo.
5.  **Simulação em Produção:** Implantação do modelo como uma API REST para inferência.

## 💾 Dataset: CIFAR-10

O CIFAR-10 é um dataset padrão em Machine Learning para classificação de imagens.

* **Conteúdo:** 60.000 imagens coloridas de 32x32 pixels.
* **Divisão:** 50.000 imagens para treinamento e 10.000 para teste.
* **Classes:** As imagens são distribuídas uniformemente entre 10 classes distintas:
    * `avião`
    * `automóvel`
    * `pássaro`
    * `gato`
    * `cervo`
    * `cachorro`
    * `sapo`
    * `cavalo`
    * `navio`
    * `caminhão`

## 🧠 Arquitetura e Treinamento da CNN

Foi desenvolvida e treinada uma Rede Neural Convolucional (CNN) personalizada para este problema de classificação.

### Data Augmentation

Para melhorar a robustez e a capacidade de generalização do modelo, aplicou-se **Data Augmentation**. Técnicas como rotação, deslocamento horizontal/vertical e inversão horizontal foram utilizadas para criar variações sintéticas das imagens de treinamento. Isso ajuda a prevenir o *overfitting* e a expor o modelo a uma maior diversidade de exemplos.

### Desempenho do Modelo

Após o treinamento, o modelo alcançou uma acurácia de aproximadamente **71.63%** no conjunto de teste. Este resultado demonstra a capacidade do modelo em classificar corretamente a maioria das imagens, mesmo com as limitações de resolução do dataset CIFAR-10 e sem o uso de técnicas de *fine-tuning* em modelos pré-treinados complexos.

## 🚀 Simulação em Produção: API REST

Para simular o uso do modelo em um ambiente real, foi desenvolvida uma API REST simples utilizando Flask. Esta API permite que outras aplicações enviem uma imagem via requisição HTTP POST e recebam a predição da classe como resposta.

### Endpoint da API

* **URL:** `/predict`
* **Método:** `POST`
* **Corpo da Requisição (Body):** `multipart/form-data` contendo um campo `file` com a imagem a ser classificada.
* **Exemplo de Resposta (JSON):**
    ```json
    {
      "all_probabilities": [0.9958796501159668, 2.7326239433023147e-05, ..., 1.3534101526602171e-05],
      "confidence": 0.9958796501159668,
      "prediction": "avião"
    }
    ```

## 🛠️ Como Executar o Projeto

### Pré-requisitos

* Python 3.8+
* Pip (gerenciador de pacotes do Python)

### Passos para Configuração e Execução

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/Eduardochimchek/cifar10-cnn-classifier.git](https://github.com/Eduardochimchek/cifar10-cnn-classifier.git)
    cd cifar10-cnn-classifier
    ```
    (Se você ainda não tem um repositório, basta navegar até a pasta do projeto.)

2.  **Crie e Ative um Ambiente Virtual:**
    É altamente recomendável usar um ambiente virtual para gerenciar as dependências do projeto.
    ```bash
    python -m venv .venv
    ```
    * **Windows PowerShell:**
        ```bash
        .\.venv\Scripts\Activate.ps1
        ```
    * **Windows Command Prompt:**
        ```bash
        .\.venv\Scripts\activate.bat
        ```
    * **Linux / macOS:**
        ```bash
        source ./.venv/bin/activate
        ```

3.  **Instale as Dependências da API:**
    Navegue até a pasta `api` e instale as bibliotecas necessárias.
    ```bash
    cd api
    pip install -r requirements.txt
    ```
    **(Opcional):** Se for usar o `test_api_troubleshoot.py`, instale também `requests`:
    ```bash
    pip install requests
    ```

4.  **Execute a API Flask:**
    No terminal, estando dentro da pasta `api` com o ambiente virtual ativado:
    ```bash
    python app.py
    ```
    A API será iniciada e ficará disponível em `http://0.0.0.0:5000`.

5.  **Teste a API:**

    * **Usando o script Python (Recomendado para verificar funcionalidade):**
        Abra um **novo terminal**, ative o ambiente virtual, navegue para a **raiz do projeto** e execute:
        ```bash
        # Certifique-se de ter uma imagem de teste (ex: aviao.jpg) na raiz do projeto.
        python test_api_troubleshoot.py
        ```
        Você deverá ver a previsão no console.

    * **Usando a Extensão Rest Client (VS Code):**
        1.  No VS Code, abra o arquivo `test_predict.http` localizado na pasta `api/`.
        2.  **Certifique-se de que o caminho da imagem no arquivo `.http` esteja correto:**
            ```http
            file=@C:/caminho/completo/para/sua/imagem_de_teste.jpg
            # Ex: file=@C:/Users/T-GAMER/Documents/GitHub/cifar10-cnn-classifier/aviao.jpg
            ```
            Ou, se a imagem estiver na raiz do projeto:
            ```http
            file=@../aviao.jpg
            ```
        3.  Clique no link "Send Request" (ou ícone de play) acima da requisição.

## 🤝 Contribuição

Sinta-se à vontade para explorar, modificar e aprimorar este projeto. Sugestões e contribuições são bem-vindas!

## 📄 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.