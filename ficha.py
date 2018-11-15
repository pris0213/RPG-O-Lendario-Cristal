class Ficha:

  def __init__(self, nome, habilidade, raca, sacola = []):
    self.nome = nome
    self.habilidade = habilidade
    self.raca = raca
    self.sacola = sacola

  @property
  def nome(self):
    return self.__nome 

  @property 
  def habilidade(self):
    return self.__habilidade
  
  @property
  def raca(self):
    return self.__raca

  @property
  def sacola(self):
    return self.__sacola

  @nome.setter 
  def nome(self, nome):
    if (not nome):
      self.__nome = "Cacá de Oliveira"
    self.__nome = nome

  @habilidade.setter 
  def habilidade(self, habilidade):
    if (not habilidade):
      self.__habilidade = "guerra"
    self.__habilidade = habilidade

  @raca.setter
  def raca(self, raca):
    if (not raca):
      self.__raca = "humana"
    self.__raca = raca
  
  @sacola.setter 
  def sacola(self, sacola):
    self.__sacola = ["Mapa","Poção de Alecrim", "Papel de Bala"]
