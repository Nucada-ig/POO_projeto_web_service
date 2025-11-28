from flask import Blueprint, request, jsonify
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
## chega perto de bug por excesso 
@aprovacao_bp.route("/aplicante/aprovar/<int:id>", methods=["POST"])
def aprovar(id):
    conn = sqlite3.connect("aplicantes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM aplicantes WHERE id = ?", (id,))
    dados = cursor.fetchone()

    # mover para outro banco
    tipo = dados[5]  # entregador, atendente ou gerente
    db_destino = f"{tipo}.db"

    conn2 = sqlite3.connect(db_destino)
    c2 = conn2.cursor()
    c2.execute("INSERT INTO usuarios VALUES (?,?,?,?,?,?)", dados)

    conn2.commit()
    conn2.close()

    cursor.execute("DELETE FROM aplicantes WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return jsonify({"mensagem": "Aplicante aprovado"}), 200


# Recusar aplicante
@aprovacao_bp.route("/aplicante/recusar/<int:id>", methods=["POST"])
def recusar(id):
    conn = sqlite3.connect("aplicantes.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM aplicantes WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Aplicação recusada"}), 200
