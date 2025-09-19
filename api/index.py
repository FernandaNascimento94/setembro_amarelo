import random
from flask import Flask, jsonify
from api.carregar_mensagens import carregar_mensagens

mensagens_motivacionais = carregar_mensagens("bancodemensagens.csv")
app = Flask(__name__)

# codigo de exemplo do vercel
# @app.route('/')
# def home():
#     return 'Hello, World!'

# @app.route('/about')
# def about():
#     return 'About'

@app.route("/", methods=['GET'])
def sortear_mensagem():
    """
    Este endpoint sorteia e retorna uma mensagem motivacional da lista.
    """
    # Verifica se a lista de mensagens não está vazia
    if not mensagens_motivacionais:
        return jsonify({"erro": "Nenhuma mensagem foi carregada."}), 500

    # Escolhe uma mensagem de forma aleatória da lista
    mensagem_escolhida = random.choice(mensagens_motivacionais)

    # Cria um dicionário para a resposta JSON
    resposta = {
        "mensagem": mensagem_escolhida
    }

    # Retorna o dicionário em formato JSON
    return jsonify(resposta)