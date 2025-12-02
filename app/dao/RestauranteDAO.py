import sqlite3

class RestauranteDAO:
    def __init__(self, db_path='app/database/app.db'):
        self.db_path = db_path
        self._criar_tabela()

    def _conectar(self):
        conn = sqlite3.connect(self.db_path)
        conn.execute("PRAGMA foreign_keys = ON;")
        return conn

    def _criar_tabela(self):
        conn = self._conectar()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS restaurantes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                endereco TEXT NOT NULL,
                telefone TEXT NOT NULL,
                email TEXT NOT NULL,
                cnpj TEXT UNIQUE NOT NULL,
                nome_responsavel TEXT NOT NULL,
                codigo_unico INTEGER UNIQUE NOT NULL
            );
        """)
        conn.commit()
        conn.close()

    def inserir(self, restaurante):
        conn = self._conectar()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO restaurantes (nome, endereco, telefone, CNPJ, email, nome_responsavel, codigo_unico)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (restaurante.nome, restaurante.endereco, restaurante.telefone, restaurante.CNPJ, restaurante.email, restaurante.nome_responsavel, restaurante.codigo_unico))
        conn.commit()
        conn.close()

    def remover(self, id_restaurante):
        conn = self._conectar()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM restaurantes WHERE id=?", (id_restaurante,))
        conn.commit()
        conn.close()

    def procurar_um(self, id_restaurante):
        conn = self._conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM restaurantes WHERE id=?", (id_restaurante,))
        dado = cursor.fetchone()
        conn.close()
        return dado
    
    def procurar_por_usuario(self, username):
        conn = self._conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM restaurantes WHERE username=?", (username,))
        dados = cursor.fetchall()
        conn.close()
        return dados

    def procurar_todos(self):
        conn = self._conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM restaurantes")
        dados = cursor.fetchall()
        conn.close()
        return dados
    
    def procurar_por_codigo(self, codigo_unico):
        conn = self._conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM restaurantes WHERE codigo_unico=?", (codigo_unico,))
        dados = cursor.fetchone()
        conn.close()
        return dados
    def procurar_por_nome(self, nome):
        conn = self._conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM restaurantes WHERE nome=?", (nome,))
        dados = cursor.fetchall()
        conn.close()
        return dados

