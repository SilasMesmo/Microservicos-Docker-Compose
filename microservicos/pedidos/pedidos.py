from flask import Flask, jsonify, render_template

# app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates')) não funcionou
app = Flask(__name__) 

PEDIDOS_DB = [
    {"id": 1, "item": "Hambúrguer Clássico", "status": "Preparando"},
    {"id": 2, "item": "Fritas Grande", "status": "Entregue"}
]

@app.route('/pedidos', methods=['GET'])
def listar_pedidos():
    return jsonify(PEDIDOS_DB), 200

@app.route('/', methods=['GET'])
def home():
    return render_template('pedidos.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
