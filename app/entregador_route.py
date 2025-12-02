from flask import Blueprint, jsonify
import sqlite3

entregador_bp = Blueprint("entregadores", __name__)

# Buscar entregador específico
@entregador_bp.route("/entregador/<int:id>", methods=["GET"])
def ver_entregador(id):
    conn = sqlite3.connect("entregadores.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM entregadores WHERE id = ?", (id,))
    dados = cursor.fetchone()
    conn.close()
    return jsonify(dados), 200


# Listar todos
@entregador_bp.route("/entregadores", methods=["GET"])
def listar_entregadores():
    conn = sqlite3.connect("entregadores.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM entregadores")
    dados = cursor.fetchall()
    conn.close()
    return jsonify(dados), 200
