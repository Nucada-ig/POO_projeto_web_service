class Restaurante:
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
