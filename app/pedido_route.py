from flask import Blueprint, request, jsonify
import sqlite3

pedido_bp = Blueprint("pedido", __name__)

# Adicionar pedido
@pedido_bp.route("/pedido/novo", methods=["POST"])
def novo_pedido():
    ################ temp
    dados = request.json
    ################ criar função que coleta os dados do pedido
    conn = sqlite3.connect("pedidos.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO pedidos (numero, preco, observacao, pagamento, status)
        VALUES (?, ?, ?, ?, ?)
    """, (dados["numero"], dados["preco"], dados["observacao"], dados["pagamento"], dados["status"]))

    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Pedido criado"}), 201


# Visualizar informações de um pedido
@pedido_bp.route("/pedido/<int:numero>", methods=["GET"])
def visualizar_pedido(numero):
    conn = sqlite3.connect("pedidos.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pedidos WHERE numero = ?", (numero,))
    pedido = cursor.fetchone()

    conn.close()
    return jsonify(pedido), 200


# Listar apenas pedidos não concluídos
@pedido_bp.route("/pedidos/ativos", methods=["GET"])
def pedidos_ativos():
    conn = sqlite3.connect("pedidos.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pedidos WHERE status != 'entregue'")
    pedidos = cursor.fetchall()

    conn.close()
    return jsonify(pedidos), 200


# Atualizar status do pedido
@pedido_bp.route("/pedido/status/<int:numero>", methods=["POST"])
def atualizar_status(numero):
    ################ temp
    novo_status = request.json["status"]
    ################ criar função que coleta o novo status do pedido, ou automatizar, testar o impacto de um contador
    conn = sqlite3.connect("pedidos.db")
    cursor = conn.cursor()

    cursor.execute("UPDATE pedidos SET status = ? WHERE numero = ?", (novo_status, numero))

    conn.commit()
    conn.close()
    return jsonify({"mensagem": "Status atualizado"}), 200
