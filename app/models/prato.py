class Prato:
  seq = 0
  def __init__(self, nome, descricao_prato, valor_prato, tipo_prato, status_prato="ativo", id_prato = None):
    self.__id_prato = id_prato
    self.__descricao_prato = descricao_prato
    self.__valor_prato = valor_prato
    self.__tipo_prato = tipo_prato
    self.__status_prato = status_prato
    self.__nome = nome

    self.__class__.seq += 1
    self.__id_prato = self.__class__.seq

  @property
  def id_prato(self):
    return self.__id_prato

  @property
  def nome(self):
    return self.__nome
  @nome.setter
  def nome(self, novo_nome):
    self.__nome = novo_nome

  @property
  def id_prato(self):
    return self.__id_prato
  @id_prato.setter
  def id_prato(self, novo_id):
    raise ValueError("Não é possível alterar o ID de um prato")

  @property
  def descricao_prato(self):
    return self.__descricao_prato
  @descricao_prato.setter
  def descricao_prato(self, nova_descricao):
    self.__descricao_prato = nova_descricao

  @property
  def valor_prato(self):
    return self.__valor_prato
  @valor_prato.setter
  def valor_prato(self, novo_valor):
    if novo_valor >= 0:
      self.__valor_prato = novo_valor
    else:
      print("Erro: O valor do prato não pode ser negativo.")

  @property
  def tipo_prato(self):
    return self.__tipo_prato
  @tipo_prato.setter
  def tipo_prato(self, novo_tipo):
    self.__tipo_prato = novo_tipo

  @property
  def status_prato(self):
    return self.__status_prato
  @status_prato.setter
  def status_prato(self, novo_status):
    status_validos = ["ativo", "inativo", "esgotado"]
    if novo_status in status_validos:
      self.__status_prato = novo_status
    else:
      print(f"Erro: '{novo_status}' não é um status válido.")