from flask import Blueprint, request, jsonify, redirect, url_for, render_template
from .dao.AplicantesDAO import AplicanteDAO
import sqlite3

aprovacao_bp = Blueprint("aprovacao", __name__)

# Painel de aprovação
@aprovacao_bp.route("/painel_aprovacao", methods=["GET"])
def painel_aprovacao():
    return render_template("aguardando_aprovacao.html")

# Ver aplicantes
@aprovacao_bp.route("/aplicantes", methods=["GET"])
def listar_aplicantes():
    conn = sqlite3.connect("aplicantes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM aplicantes")
    lista = cursor.fetchall()
    conn.close()
    return jsonify(lista), 200


# Aprovar aplicante
@aprovacao_bp.route("/aplicante/aprovar/<int:id>", methods=["POST"])
def aprovar(id):

    tipo_destino = request.form['tipo']  # entregador, atendente, gerente

    aplicante = AplicanteDAO.buscar(id)

    AplicanteDAO.aprovar(aplicante, tipo_destino)

    return redirect(url_for("usuario.usuario_aprovacao"))



# Recusar aplicante
@aprovacao_bp.route("/aplicante/recusar/<int:id>", methods=["POST"])
def recusar(id):

    justificativa = request.form.get('motivo', '')  # se quiser usar

    AplicanteDAO.remover(id)

    return redirect(url_for("usuario.usuario_aprovacao"))
