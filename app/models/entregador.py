class Usuario_class:
    def __init__(self, nome, cpf, email, telefone, username, password, tipo):
        self.__nome = nome
        self.__cpf = cpf
        self.__email = email
        self.__telefone = telefone
        self.__username = username
        self.__password = password
        self.__tipo = tipo

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def telefone(self):
        return self.__telefone
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone

    @property
    def endereco(self):
        return self.__endereco
    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username):
        self.__username = username
    
    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

class Entregador(Usuario_class):
    def __init__(self, nome, email, senha, CPF, tipo, veiculo, status):
        super().__init__(nome, email, senha, CPF, tipo)
        self.__veiculo = veiculo
        self.__status = status

    @property
    def veiculo(self):
        return self.__veiculo

    @veiculo.setter
    def veiculo(self, veiculo):
        self.__veiculo = veiculo

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        if status in ['disponível', 'em rota', 'off-line', 'voltando']:
            self.__status = status
        else:
            raise ValueError("O valor do status deve ser 'disponível', 'em rota', 'off-line' ou 'voltando'.")