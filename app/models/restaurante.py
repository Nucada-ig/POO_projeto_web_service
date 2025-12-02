import random
class Restaurante:
    def __init__(self, nome, endereco, telefone, CNPJ, email, nome_responsavel, codigo_unico=None):
        if codigo_unico is None:
            codigo_unico = random.randint(100000, 999999)
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone
        self.__CNPJ = CNPJ
        self.__email = email
        self.__codigo_unico = codigo_unico
        self.__nome_responsavel = nome_responsavel

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
    
    @property
    def nome_responsavel(self):
        return self.__nome_responsavel

    @nome_responsavel.setter
    def nome_responsavel(self, nome_responsavel):
        self.__nome_responsavel = nome_responsavel
    
    @property
    def codigo_unico(self):
        return self.__codigo_unico
    @codigo_unico.setter
    def codigo_unico(self):
        self.__codigo_unico = random.randint(100000, 999999)
