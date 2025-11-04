FROM python:3.10-slim

WORKDIR /app

# 1. Copia o arquivo de dependências
COPY requirements.txt .

# 2. Instala as dependências (Flask)
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copia o código da aplicação (login.py)
COPY . .

# 4. Documenta a porta que a aplicação usa
EXPOSE 8080 

# 5. Comando para executar a aplicação com o nome correto
CMD ["python", "login.py"]
