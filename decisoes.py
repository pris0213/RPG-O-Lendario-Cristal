import random

def decisao_1():
  print("   O QUE VOCÊ IRÁ FAZER?\n\n" +
  "   |♢| SEGUIR VIAGEM (INSIRA \'1\')\n" +
  "   |♢| SE HOSPEDAR NO HOTEL A LESTE DO VILAREJO E TIRAR UMAS FÉRIAS (INSIRA \'2\')\n" +
  "   |♢| IR PARA CASA JOGAR LOLZINHO (INSIRA \'3\')\n")

  return int(input())

# Criar personagem - Raça
def decisao_2():
  print("   QUAL SERÁ A SUA RAÇA?\n\n" +
  "   |♢| CENTAURO\n" +
  "   |♢| ELFO\n" +
  "   |♢| GNOMO\n" +
  "   |♢| HUMANA\n" +
  "   |♢| ORC\n" +
  "   |♢| SEREIA\n")

  decisao = input()
  if (not decisao):
    decisao = "humana"
  return decisao

def decisao_3():
  print("   QUAL SERÁ A SUA HABILIDADE?\n\n" +
  "   |♢| ARTES MARCIAIS\n" +
  "   |♢| CURA\n" +
  "   |♢| DRUIDISMO\n" +
  "   |♢| GUERRA\n" +
  "   |♢| MAGIA\n" +
  "   |♢| MÚSICA\n")

  decisao = input()
  if (not decisao):
    decisao = "guerra"
  return decisao

def decisao_4():
  print("   PELAS BARBAS DE MERLIN, COMO DEVO LHE CHAMAR?\n")

  decisao = input()
  if (not decisao):
    decisao = "cacá"
  return decisao

def decisao_5():
  print("   VOCÊ PODE ESCOLHER APENAS UM ITEM ABAIXO\n\n" +
  "   |♢| ARCO E FLECHA\n" +
  "   |♢| BANJO\n" +
  "   |♢| CETRO \n" +
  "   |♢| CINTO SALVA-VIDAS DA LENDÁRIA DRUIDA FREYA\n" +
  "   |♢| ESPADA\n" +
  "   |♢| LANÇA\n\n" +
  "   (Informe apenas a primeira palavra do item desejado.)")
  
  decisao = input().lower()
  if (not decisao):
    decisao = "Espada"
  elif (decisao == "arco" or decisao == "arco e flecha"):
    decisao = "Arco e Flecha"
  elif (decisao == "cinto salva-vidas da lendária druida freya" or decisao == "cinto salva-vidas da lendaria druida freya" or decisao == "cinto salva vidas da lendaria druida freya" or decisao == "cinto salva vidas da lendária druida freya" or decisao == "cinto"):
    decisao = "Cinto Salva-Vidas da Lendária Druida Freya"
  else:
    decisao = decisao.capitalize()
  
  return decisao

def decisao_6():
  print("   PARA QUAL DIREÇÃO DESEJA SEGUIR?\n\n" +
  "   |♢| NORTE\n" +
  "   |♢| SUL\n" +
  "   |♢| LESTE\n" +
  "   |♢| OESTE\n")
  decisao = input().lower()
  if (decisao == "sul" or decisao == "s" or decisao == "south"):
    decisao = "sul"
  elif (decisao == "leste" or decisao == "l" or decisao == "e" or decisao == "east"):
    decisao = "leste"
  elif (decisao == "oeste" or decisao == "o" or decisao == "w" or decisao == "west"):
    decisao = "oeste"
  else:
    decisao = "norte"
  
  return decisao

def decisao_7(personagem):
  print("   SUA SACOLA ESTÁ CHEIA. PARA GUARDAR 𝓞 𝓛𝓮𝓷𝓭𝓪𝓻𝓲𝓸 𝓒𝓻𝓲𝓼𝓽𝓪𝓵, ESCOLHA UM ITEM PARA JOGAR FORA\n\n" +
  "   |♢| " + personagem.sacola[0].upper() + "\n" +
  "   |♢| " + personagem.sacola[1].upper() + "\n" +
  "   |♢| " + personagem.sacola[2].upper() + "\n" +
  "   |♢| " + personagem.sacola[3].upper() + "\n\n" +
  "   (Informe apenas a primeira palavra do item desejado.)")
  
  decisao = input().lower()

  if (decisao == "mapa"):
    decisao = 0
  elif (decisao == "poção" or decisao == "pocao" or decisao == "pocao de alecrim" or decisao == "poção de alecrim"):
    decisao = 1
  elif (decisao == "papel" or decisao == "papel de bala"):
    decisao = 2
  else:
    decisao = 3
  
  return decisao

def decisao_8(personagem):
  vida_do_minotauro = 10
  barrinha_de_vida_do_minotaro = "⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛"
  ataque = 0
  desistiu = False
  while ((not desistiu) and (vida_do_minotauro > 0)):
    print(
      "   [ MINOTAURO HP " + barrinha_de_vida_do_minotaro + " ]\n\n")
    print(
      "   ESCOLHA SUA AÇÃO\n\n" +
      "   |♢| ATACAR (INSIRA \'A\')\n" +
      "   |♢| DESISTIR (INSIRA \'D\')\n"
    )
    decisao = input().lower()

    if (decisao == "a"):
      # Aleatório
      ataque = random.randrange(2,5)
      print(
        "   VOCÊ TIROU " + str(ataque) + " DE HP!\n\n")
      vida_do_minotauro = vida_do_minotauro - ataque
      barrinha_de_vida_do_minotaro = ""
      for cont in range(vida_do_minotauro):
        barrinha_de_vida_do_minotaro = barrinha_de_vida_do_minotaro + "⬛"
    else:
      desistiu = True
  return desistiu

def decisao_morrer():
  print("                ╭───────╯•╰───────╮\n\n")
  print("                    ᴠᴏᴄᴇ ᴍᴏʀʀᴇᴜ.")
  print("                ╰───────╮•╭───────╯\n\n")