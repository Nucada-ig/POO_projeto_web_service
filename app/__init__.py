from flask import Flask

def create_app():
    app = Flask(__name__, template_folder='view')
    app.secret_key = 'your_secret_key_here'  # Required for sessions

    from app.routes_public import public_bp
    from app.routes_restaurante import restaurante_bp
    from app.routes_cadastro_usuario import usuario_bp as cadastro_bp
    from app.usuario_route import usuario_bp
    from app.perfil_routes import perfil_bp
    from app.pedido_route import pedido_bp
    from app.prato_route import prato_bp
    from app.entregador_route import entregador_bp
    from app.aprovacao_route import aprovacao_bp

    app.register_blueprint(public_bp)
    app.register_blueprint(restaurante_bp, url_prefix='/restaurante')
    app.register_blueprint(cadastro_bp, name='cadastro')
    app.register_blueprint(usuario_bp, name='usuario')
    app.register_blueprint(perfil_bp)
    app.register_blueprint(pedido_bp)
    app.register_blueprint(prato_bp)
    app.register_blueprint(entregador_bp)
    app.register_blueprint(aprovacao_bp)

    return app
