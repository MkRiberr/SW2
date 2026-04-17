from flask import Flask, jsonify
import os

app = Flask(__name__)

produtos = [
    {"id": 1, "nome": "Notebook"},
    {"id": 2, "nome": "Mouse"},
    {"id": 3, "nome": "Teclado"},
]

@app.route("/produtos", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de Produtos - Acesse /produtos"})

@app.route("/", methods=["GET"])
def listar_produtos():
    return jsonify(produtos)

if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0", port=port)