from flask import Flask

def create_app():
    app = Flask(__name__, template_folder='view')

    from app.routes_public import public_bp
    from app.routes_restaurante import restaurante_bp
    from app.routes_cadastro_usuario import usuario_bp

    app.register_blueprint(public_bp)
    app.register_blueprint(restaurante_bp, url_prefix='/restaurante')
    app.register_blueprint(usuario_bp)

    return app
