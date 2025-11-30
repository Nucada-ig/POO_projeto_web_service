from app.models.endereco import Endereco
class Cliente:
  seq = 0
  def __init__(self, nome, telefone, id = None):

    self.__nome = nome
    self.__telefone = telefone
    self.__id = id
    self.__endereco = []

    self.__class__.seq += 1
    self.__id = self.__class__.seq

  @property
  def nome(self):
    return self.__nome
  @nome.setter
  def nome(self, nome):
    self.__nome = nome

  @property
  def telefone(self):
    return self.__telefone
  @telefone.setter
  def telefone(self, telefone):
    self.__telefone = telefone

  @property
  def id(self):
    return self.__id
  @id.setter
  def id(self, id):
    raise ValueError('Não é possível alterar o ID de um cliente')

  #associação simples x restaurante
  @property
  def restaurante(self):
      return self._restaurante
  @restaurante.setter
  def restaurante(self, value):
      self._restaurante = value
  #composição x endereço
  @property
  def endereço(self):
      return self._endereco

  def adicionar_endereco(self, estado, cidade, setor, rua, numero, complemento):
    endereco = Endereco(estado, cidade, setor, rua, numero, complemento)
    self._endereco.append(endereco)
