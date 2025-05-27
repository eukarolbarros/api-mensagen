from flask import Blueprint, jsonify

messages_bp = Blueprint('messages', __name__) #criou um blueprint

@messages_bp.route("/", methods=["GET"])
def get_messages(): #retorna lista de mensagens, json
    messages = Message.query.order_by(Message.created_at.desc()).all() # busca todas as mensagens da tabela no bd e organiza da mais recente para a mais antiga, o for msg in menssages tranforma cada obj em um dicionario
    return jsonify([msg.to_dict() for msg in messages])

    