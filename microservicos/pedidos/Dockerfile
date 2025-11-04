FROM python:3.10-slim

WORKDIR /app

# 1. Copia o arquivo de dependências
COPY requirements.txt .

# 2. Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copia o código da aplicação (o nome mudou para app.py)
COPY . .

# 4. porta que a aplicação usa
EXPOSE 8081 

# 5. Comando para executar a aplicação
CMD ["python", "pedidos.py"]
