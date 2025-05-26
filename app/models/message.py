from datetime import datetime
from app import db

class Message(db.Model): #db.model, ta no flask ja,facilitar o processo 
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self): #tranforma o objeto em forma de dicionario pro json
        return {
            "id": self.id,
            "content": self.content,
            "created_at": self.created_at.isoformat()
        }
    
#mensagem = Message.query.find(1) - se tiver uma mensagem com o id ele cria uma instancia e atribui a variavel mensagem - tem todos os dados do id 1 
#to dict retorna um dicionario com os dados da mensagem id 1
#mensagem_dict = mensagem.to_dict() - recebe dados em forma de dicionario