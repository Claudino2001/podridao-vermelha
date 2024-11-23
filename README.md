<h1 align="center">
    <strong>SISTEMA DE DETECÇÃO DO FUNGO DA PODRIDÃO VERMELHA NA PLANTA AGAVE</strong>
</h1>

## Sobre

Desenvolver um sistema de visão computacional especializado e eficiente para a Área de Design e Produto Industrial (DPI) do Senai CIMATEC para uso em mudas de AGAVE, visando a identificação precoce da podridão vermelha. A proposta deste projeto visa trazer um sistema que utilizará algoritmos para o processamento, análise e certificação de imagens coletadas e entregues à equipe técnica do projeto. 

## Instruções de Uso do Sistema de Detecção de Fungos

Este sistema permite o envio de uma imagem para detecção de fungos com base em um modelo pré-treinado.

### Como Configurar o Servidor

1. **Requisitos do Sistema**
   - Python 3.8 instalado.
   - Dependências necessárias:
     - Flask
     - TensorFlow
     - Pillow

   Execute o seguinte comando para instalar todas as dependências:
   ```bash
   pip install -r requirements.txt
   ```

2. **Iniciar o Servidor**
   - Ative o ambiente virtual (se aplicável):
     ```bash
     .\.venv\Scripts\activate
     ```
   - Inicie o servidor Flask com o seguinte comando:
     ```bash
     python app.py
     ```

3. **Verificar Funcionamento**
   - O servidor estará disponível no endereço:
     ```
     http://127.0.0.1:5000/
     ```
### Como Configurar o Servidor Usando Docker

1. **Instalar o Docker no seu Computador**  
   Baixe e instale o Docker Desktop em sua máquina.  
   [Download do Docker Desktop para Windows](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-win-amd64)

2. **Baixe o serviço da rede neural em sua máquina**  
   Após a instalação do Docker, faça o download da imagem do serviço da rede neural com o comando:  
   ```bash
   docker pull claudino2001/service-agave
   ```

3. **Execute o serviço para deixá-lo online em sua rede local**  
   Após o download, execute o seguinte comando para rodar o serviço na sua rede local, ouvindo na porta 5000:  
   ```bash
   docker run -p 5000:5000 claudino2001/service-agave
   ```
   Isso vai deixar o serviço acessível em `http://localhost:5000`.



## Como Utilizar a Ferramenta

### Frontend (Página da Web)
1. Acesse a página de upload pelo navegador (front/index.html). Dentro da pasta "front", abra o arquivo "index.html" usando o navegador de sua preferência.
3. Clique no botão "Choose File" ou "Selecionar Arquivo" para enviar uma imagem.
4. Clique no botão "Enviar".
5. Aguarde a análise.
6. O resultado da análise será exibido logo abaixo do botão 'Enviar', indicando se há ou não a presença do fungo e a confiança da predição.
<p align="center">
    <img src="https://github.com/user-attachments/assets/75d0247b-4170-4b5b-85eb-8a0115118a64">
</p>

### Via Ferramenta de Teste (Postman ou Similar)
1. Abra a ferramenta de testes.
2. Configure uma requisição POST para o endpoint:
   ```
   http://127.0.0.1:5000/detecta-fungo
   ```
3. No corpo da requisição, selecione a opção `form-data`:
   - **Key:** `file`
   - **Value:** Faça upload da imagem desejada.
4. Clique em "Enviar" para obter a resposta.

## Possíveis Problemas e Soluções
- **Erro de Conexão com o Servidor**
  - Certifique-se de que o servidor está em execução.
  - Verifique se o endereço e a porta estão corretos.
  -  Certifique-se de que o servidor e o Frontend estão executando na mesma rede.

- **Imagem Não Reconhecida**
  - Certifique-se de enviar uma imagem no formato JPEG ou PNG.
  - Certifique-se de que a imagem contém conteúdo relevante para a análise.

## Personalizações
Se precisar personalizar, ajustar o sistema para outro modelo, adicionar funcionalidade ou retreinar a rede neural, entre em contato conosco.

Atenciosamente,

Equipe de Desenvolvimento.

- [Davi Nogueira Gonçalves](https://github.com/)  
- [Igor Souza Freitas](https://github.com/IgorSF01)  
- [Gabriel De Araujo Claudino](https://github.com/Claudino2001)  
- [José Santos Damasceno](https://github.com/jos756H)  
- [Lucas Amparo Barbosa](https://github.com/lucasamparo)
