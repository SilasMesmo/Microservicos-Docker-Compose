from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

#simulação de base de dados
USUARIOS_DB = {
    "admin": "12345",
    "joao": "senhafraca"
}

#mostrar o formulário
@app.route('/', methods=['GET'])
def mostrar_formulario():
    return render_template('login.html') 

@app.route('/login', methods=['POST'])
def fazer_login():
    
    dados = request.get_json()
    usuario = dados.get('usuario')
    senha = dados.get('senha')

    if USUARIOS_DB.get(usuario) == senha:
        return jsonify({"mensagem": f"Login bem-sucedido! Bem-vindo(a), {usuario}!"}), 200
    else:
        return jsonify({"mensagem": "Credenciais inválidas."}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
