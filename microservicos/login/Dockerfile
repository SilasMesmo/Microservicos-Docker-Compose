FROM python:3.10-slim

WORKDIR /app

# 1. Copia o arquivo de dependências
COPY requirements.txt .

# 2. Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copia o código da aplicação
COPY . .

# 4. Documenta a porta que a aplicação usa
EXPOSE 8080 

# 5. Comando para executar a aplicação
CMD ["python", "login.py"]
