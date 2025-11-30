from flask import Blueprint, request, jsonify, redirect, url_for
from dao.Aplicante_dao import dao_Aplicantes
from dao.Aprovacao_dao import dao_Aprovacao
import sqlite3

aprovacao_bp = Blueprint("aprovacao", __name__)

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

    aplicante = dao_Aplicantes.buscar(id)

    dao_Aprovacao.aprovar(aplicante, tipo_destino)

    return redirect(url_for("usuario.usuario_aprovacao"))



# Recusar aplicante
@aprovacao_bp.route("/aplicante/recusar/<int:id>", methods=["POST"])
def recusar(id):

    justificativa = request.form.get('motivo', '')  # se quiser usar

    dao_Aplicantes.remover(id)

    return redirect(url_for("usuario.usuario_aprovacao"))
