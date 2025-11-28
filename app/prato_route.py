from flask import Blueprint, request, jsonify
import sqlite3

prato_bp = Blueprint("prato", __name__)

# Criar novo prato
@prato_bp.route("/prato/novo", methods=["POST"])
def novo_prato():
    ################ temp
    dados = request.json
    ################ criar função que coleta os dados do prato
    conn = sqlite3.connect("pratos.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO pratos (valor, tipo, descricao, id, status, nome)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (dados["valor"], dados["tipo"], dados["descricao"], dados["id"], dados["status"], dados["nome"]))

    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Prato criado"}), 201


# Ver prato por ID
@prato_bp.route("/prato/<int:id>", methods=["GET"])
def ver_prato(id):
    conn = sqlite3.connect("pratos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pratos WHERE id = ?", (id,))
    prato = cursor.fetchone()
    conn.close()
    return jsonify(prato), 200


# Listar pratos ativos
@prato_bp.route("/pratos/ativos", methods=["GET"])
########## tem que listar todos os pratos, não só os ativos para poderem ser editados depois
def pratos_ativos():
    conn = sqlite3.connect("pratos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pratos WHERE status = 'ativo'")
    pratos = cursor.fetchall()
    conn.close()
    return jsonify(pratos), 200


# Alterar status
@prato_bp.route("/prato/status/<int:id>", methods=["POST"])
def alterar_status(id):
    ################ temp
    status = request.json["status"]
    ################ criar função que coleta o novo status do prato ou automatizar, testar o impacto de um contador
    conn = sqlite3.connect("pratos.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE pratos SET status = ? WHERE id = ?", (status, id))

    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Status alterado"}), 200


# Remover prato
@prato_bp.route("/prato/remover/<int:id>", methods=["POST"])
def remover_prato(id):
    conn = sqlite3.connect("pratos.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM pratos WHERE id = ?", (id,))

    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Prato removido"}), 200
