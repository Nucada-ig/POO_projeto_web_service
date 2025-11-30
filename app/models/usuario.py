class usuario:
    def __init__(self, nome, email, senha, CPF, tipo):
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__CPF = CPF
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
    def senha(self):
        return self.__senha
    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @property
    def CPF(self):
        return self.__CPF
    @CPF.setter
    def CPF(self, CPF):
        self.__CPF = CPF

    @property
    def tipo(self):
        a = self.__tipo
        if a == 0 :
            return 'Usuário com cargo de entregador(0)'
        elif a == 1:
            return 'Usuário com cargo de atendente(1)'
        elif a == 2:
            return 'Usuário com cargo de gerente(2)'
        elif a == 3:
            return 'Usuário com cargo de dono(3)'
        else:
            return "Tipo de usuário inválido"
    @tipo.setter
    def tipo(self, tipo):
        if tipo in [0, 1, 2, 3]:
            self.__tipo = tipo
        else:
            raise ValueError("O valor do tipo deve ser 0, 1, 2 ou 3.")