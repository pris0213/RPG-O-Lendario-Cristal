from ficha import *
from decisoes import *
from historia import *

historia_introducao()

escolha = decisao_1()

if (escolha == 1):
  # Cria personagem
  historia_parte_1()
  raca = decisao_2().lower()
  historia_parte_2(raca)
  habilidade = decisao_3().lower()
  historia_parte_3(raca, habilidade)
  nome = decisao_4().capitalize()
  personagem = Ficha(nome, raca, habilidade)
  # Escolhe arma ou apetrecho 
  historia_parte_4(personagem)
  item = decisao_5()
  personagem.sacola.append(item)
  historia_parte_5(personagem)
  # Escolhe direcao
  direcao = decisao_6()
  historia_parte_6(direcao)
  # Escolhe item a remover da sacola
  item_a_ser_removio = decisao_7(personagem)
  personagem = historia_parte_7(personagem, item_a_ser_removio)
  # Acaba
  morreu = decisao_8(personagem)
  if (morreu):
    decisao_morrer()
  else:
    historia_parte_8(personagem)
elif (escolha == 2):
  jogador_desistiu()
elif (escolha == 3):
  jogador_desistiu_de_forma_ridicula()

