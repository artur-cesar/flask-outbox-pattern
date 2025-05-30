# Usa uma imagem oficial do Python como base
FROM python:3.11-slim

RUN apt-get update && apt-get install -y make && rm -rf /var/libs/apt/lists/*

# Define o diretório de trabalho no container
WORKDIR /app

# Copia o arquivo de requisitos
COPY requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante da aplicação
COPY . .

# Define a porta que será exposta
EXPOSE 5000

# Comando para rodar o app
CMD ["python", "app.py"]
