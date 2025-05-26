from flask import Blueprint, jsonify

messages_bp = Blueprint('messages', __name__) #criou um blueprint

@messages_bp.route("/", methods=["GET"])
def get_messages(): #retorna lista de mensagens, json
    return jsonify({"messages": ["Olá, mundo!", "Essa é a segunda mensagem."]})