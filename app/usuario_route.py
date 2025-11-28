from flask import Blueprint, render_template

usuario_bp = Blueprint("usuario", __name__)

# Página principal do usuário — acessa todos os menus
@usuario_bp.route("/dashboard", methods=["GET"])
def usuario_home():
    return render_template("dashboard.html")

# Cada página simples
@usuario_bp.route("/pedidos", methods=["GET"])
def usuario_pedidos():
    return render_template("pedidos.html")

@usuario_bp.route("/pratos", methods=["GET"])
def usuario_pratos():
    return render_template("pratos.html")

@usuario_bp.route("/entregadores", methods=["GET"])
def usuario_entregadores():
    return render_template("entregadores.html")

@usuario_bp.route("/aprovacao", methods=["GET"])
def usuario_aprovacao():
    return render_template("aprovacao.html")

@usuario_bp.route("/config", methods=["GET"])
def usuario_config():
    return render_template("config.html")
