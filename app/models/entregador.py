from usuario import usuario
class entregador(usuario):
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