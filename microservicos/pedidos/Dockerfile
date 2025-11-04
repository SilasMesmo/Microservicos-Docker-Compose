FROM python:3.10-slim

WORKDIR /app

# 1. Copia o arquivo de dependências
COPY requirements.txt .

# 2. Instala as dependências (Flask)
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copia o código da aplicação (o nome mudou para app.py)
COPY . .

# 4. Documenta a porta que a aplicação usa
# IMPORTANTE: Use a porta 5000 para Login e 5001 para Pedidos
EXPOSE 8081 

# 5. Comando para executar a aplicação
# Nota: O host e porta estão definidos no app.py, aqui só executamos o script
CMD ["python", "pedidos.py"]
