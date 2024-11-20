# DESENVOLVIMENTO DE UM SISTEMA DE DETECÇÃO DO FUNGO DA PODRIDÃO VERMELHA NA PLANTA AGAVE

Desenvolver um sistema de visão computacional especializado e eficiente para a Área de Design e Produto Industrial (DPI) do Senai CIMATEC para uso em mudas de AGAVE, visando a identificação precoce da podridão vermelha. A proposta deste projeto visa trazer um sistema que utilizará algoritmos para o processamento, análise e certificação de imagens coletadas e entregues à equipe técnica do projeto. 

-----------

# Instruções de Uso do Sistema de Detecção de Fungos

Este sistema permite o envio de uma imagem para detecção de fungos com base em um modelo pré-treinado.

## Como Configurar o Servidor

1. **Requisitos do Sistema**
   - Python 3.8 instalado.
   - Dependências necessárias:
     - Flask
     - Keras
     - Pillow
     - NumPy

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
     http://127.0.0.1:5000
     ```

## Como Utilizar a Ferramenta

### Frontend (Página da Web)
1. Acesse a página de upload pelo navegador (link fornecido pelo cliente).
2. Clique no botão "Selecionar Arquivo" para enviar uma imagem.
3. Clique no botão "Enviar".
4. Aguarde a análise. O resultado será exibido com o nome do fungo detectado e a confiança da predição.

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
Se precisar personalizar ou ajustar o sistema para outro modelo ou funcionalidade, entre em contato conosco.

Atenciosamente,  
Equipe de Desenvolvimento
