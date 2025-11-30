from app.models.usuario import usuario
class restaurante:
    def __init__(self, nome, endereco, telefone, CNPJ, email):
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone
        self.__CNPJ = CNPJ
        self.__email = email
        self.__cardapio = []
        self.__usuarios = []

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def CNPJ(self):
        return self.__CNPJ

    @CNPJ.setter
    def CNPJ(self, CNPJ):
        self.__CNPJ = CNPJ

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

#Composição
    @property
    def usuarios(self):
        return self.__usuarios
    def adicionar_usuario(self, usuario):
        self.__usuarios.append(usuario)

    def remover_usuario(self, usuario):
        if usuario in self.__usuarios:
            self.__usuarios.remove(usuario)
        else:
            print("Usuário não encontrado neste restaurante.")

    def listar_usuarios(self):
        if self.__usuarios:
            print(f"Usuários do restaurante {self.nome}:")
            for usuario in self.__usuarios:
                print(f"- {usuario.nome} ({usuario.tipo})")

    def criar_usuario(self, nome, email, senha, CPF, tipo):
        novo_usuario = usuario(nome, email, senha, CPF, tipo)
        self.adicionar_usuario(novo_usuario)
        return novo_usuario
#agregação
    @property
    def cardapio(self):
        return self.__cardapio
    def adicionar_prato(self, prato):
        self.__cardapio.append(prato)