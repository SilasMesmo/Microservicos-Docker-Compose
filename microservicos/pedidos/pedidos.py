from flask import Flask, jsonify, render_template
# O módulo 'os' não é mais necessário

# app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))
app = Flask(__name__)  # <<<--- MUDANÇA AQUI: Removido o argumento template_folder

# Simulação de base de dados de pedidos
PEDIDOS_DB = [
    {"id": 1, "item": "Hambúrguer Clássico", "status": "Preparando"},
    {"id": 2, "item": "Fritas Grande", "status": "Entregue"}
]

# Rota para listar pedidos (JSON)
@app.route('/pedidos', methods=['GET'])
def listar_pedidos():
    return jsonify(PEDIDOS_DB), 200

# Rota para página HTML
@app.route('/', methods=['GET'])
def home():
    # Agora, o Flask procurará 'templates/pedidos.html'
    return render_template('pedidos.html')

if __name__ == '__main__':
    # A API de Pedidos rodará na porta 8081
    app.run(host='0.0.0.0', port=8081)
