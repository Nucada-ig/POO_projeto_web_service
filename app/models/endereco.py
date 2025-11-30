class Endereco:
  def __init__(self, estado, cidade, setor, rua, numero, complemento):
    self.__estado = estado
    self.__cidade = cidade
    self.__setor = setor
    self.__rua = rua
    self.__numero = numero
    self.__complemento = complemento

  @property
  def estado(self):
    return self.__estado
  @estado.setter
  def estado(self, novo_estado):
    self.__estado = novo_estado



  @property
  def cidade(self):
    return self.__cidade
  @cidade.setter
  def cidade(self, nova_cidade):
    self.__cidade = nova_cidade



  @property
  def setor(self):
    return self.__setor
  @setor.setter
  def setor(self, novo_setor):
    self.__setor = novo_setor



  @property
  def rua(self):
    return self.__rua
  @rua.setter
  def rua(self, nova_rua):
    self.__rua = nova_rua



  @property
  def numero(self):
    return self.__numero
  @numero.setter
  def numero(self, novo_numero):
    self.__numero = novo_numero



  @property
  def complemento(self):
    return self.__complemento
  @complemento.setter
  def complemento(self, novo_complemento):
    self.__complemento = novo_complemento

  def __str__(self):
    return (f"{self.rua}, {self.numero}, {self.complemento} - {self.setor}, "
          f"{self.cidade} - {self.estado}")

