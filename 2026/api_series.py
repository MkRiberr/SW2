from flask import Flask, jsonify
import os

app = Flask(__name__)

series = [
    {"id": 1, "nome": "Breaking Bad"},
    {"id": 2, "nome": "Stranger Things"},
    {"id": 3, "nome": "The Witcher"},
]

@app.route("/series", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de Séries - Acesse /series"})

@app.route("/", methods=["GET"])
def listar_series():
    return jsonify(series)

if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0", port=port)