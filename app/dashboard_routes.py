# routes/dashboard_routes.py

from flask import Blueprint, render_template, abort
from dao.PedidoDAO import PedidoDAO
from dao.UsuarioDAO import UsuarioDAO
from dao.RestauranteDAO import RestauranteDAO

dashboard_bp = Blueprint('dashboard', __name__)

pedido_dao = PedidoDAO()
usuario_dao = UsuarioDAO()
restaurante_dao = RestauranteDAO()


def _safe(value):
    """Evita None e valores inválidos."""
    try:
        return int(value)
    except:
        return 0


@dashboard_bp.route("/dashboard/<int:usuario_id>")
def dashboard(usuario_id):

    # --- Validar usuário ---
    usuario = usuario_dao.buscar_por_username  # ERRO NO SEU DAO (nota abaixo)
    conn = usuario_dao._conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id=?", (usuario_id,))
    usuario = cursor.fetchone()
    conn.close()

    if not usuario:
        abort(404, "Usuário não encontrado")

    # --- Buscar restaurante do usuário ---
    conn = restaurante_dao._conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM restaurantes WHERE usuario_id=?", (usuario_id,))
    restaurante = cursor.fetchone()
    conn.close()

    if not restaurante:
        restaurante_id = None
    else:
        restaurante_id = restaurante[0]

    # --- Carregar pedidos do restaurante ---
    if not restaurante_id:
        pedidos = []
    else:
        conn = pedido_dao._conectar()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, preco_total, status, data FROM pedidos WHERE restaurante_id=?",
            (restaurante_id,))
        pedidos = cursor.fetchall()
        conn.close()

    # --- Estatísticas ---
    total_pedidos = len(pedidos)
    entregues = len([p for p in pedidos if p[2] == 'entregue'])
    em_entrega = len([p for p in pedidos if p[2] == 'em entrega'])
    pendentes = len([p for p in pedidos if p[2] == 'pendente'])
    atrasados = len([p for p in pedidos if p[2] == 'atrasado'])

    # Proteção contra 0
    total_pedidos = _safe(total_pedidos)
    entregues = _safe(entregues)
    em_entrega = _safe(em_entrega)
    pendentes = _safe(pendentes)
    atrasados = _safe(atrasados)

    # --- Pedidos recentes ---
    recentes = sorted(pedidos, key=lambda x: x[3] or "", reverse=True)[:4]

    # --- Enviar ao HTML ---
    return render_template(
        "dashboard.html",
        total_pedidos=total_pedidos,
        entregues=entregues,
        em_entrega=em_entrega,
        pendentes=pendentes,
        atrasados=atrasados,
        recentes=recentes,
        usuario_id=usuario_id
    )

