from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__) #inicializa instancia do flask
    app.config.from_object(Config)  # (config especifica do troço)chamando metodo config, chama metodo dentro de config chamado from objesct, inicializa as configuraçoes da aplicação atraves de um objt
    
    app.json.sort_keys = False # Desativa ordenação alfabética das chaves JSON, nao bagunça o bglh, dx organizado q nem ta no bd

    db.init_app(app)  # faz a conexão entre o banco e o app Flask

    migrate.init_app(app, db) #coisas q eu envio pro banco 

    from app.models.message import Message
    # Registro de rotas
    from .routes.messages import messages_bp
    app.register_blueprint(messages_bp, url_prefix="/messages") #registra o bp, organizar as rotas
                            #ultiliza o prefixo mensagens nas rotas 
    return app