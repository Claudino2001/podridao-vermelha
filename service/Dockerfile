# Usar imagem base com Python 3.8
FROM python:3.8-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Copiar os arquivos necessários para o container
COPY requirements.txt ./
COPY app.py ./
COPY converted_keras/ ./converted_keras/

RUN pip install --no-cache-dir --upgrade pip

# Instalar dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expor a porta que o Flask usa
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["python", "app.py"]
