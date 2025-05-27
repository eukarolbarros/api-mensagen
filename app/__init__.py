from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
from flask_marshmallow import Marshmallow
from flask import jsonify
from marshmallow import ValidationError
from werkzeug.exceptions import HTTPException


db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()


def create_app():
    app = Flask(__name__) #inicializa instancia do flask
    app.config.from_object(Config)  # (config especifica do troço)chamando metodo config, chama metodo dentro de config chamado from objesct, inicializa as configuraçoes da aplicação atraves de um objt
    app.json.sort_keys = False # Desativa ordenação alfabética das chaves JSON, nao bagunça o bglh, dx organizado q nem ta no bd

    db.init_app(app)  # faz a conexão entre o banco e o app Flask
    ma.init_app(app)

    migrate.init_app(app, db) #coisas q eu envio pro banco 

    from app.models.message import Message
    
    # Registro de rotas
    from .routes.messages import messages_bp
    app.register_blueprint(messages_bp, url_prefix="/messages") #registra o bp, organizar as rotas
            
            
                            #ultiliza o prefixo mensagens nas rotas 
  # Tratadores globais de erro (explicados na seção 5.6)
    register_error_handlers(app)


    return app

def register_error_handlers(app):

    @app.errorhandler(ValidationError)
    def handle_validation_error(error):
        return jsonify({
            "error": "Validation Error",
            "messages": error.messages
        }), 400

    @app.errorhandler(HTTPException)
    def handle_http_exception(error):
        return jsonify({
            "error": error.name,
            "message": error.description
        }), error.code

    @app.errorhandler(Exception)
    def handle_generic_exception(error):
        return jsonify({
            "error": "Internal Server Error",
            "message": str(error)
        }), 500