def historia_introducao():
  print(
  "                ╭───────╯•╰───────╮\n\n" +
  "   Boas-vindas, viajante! E que longa viagem tem sido...\n\n" +
  "   Você se depara com uma placa indicando vários caminhos para os mais diversos lados e dimensões.\n\n" +
  "   É a hora de fazer um escolha. Você pretende seguir sua jornada e desvendar os mistérios que lhe aguardam ou prefere abandoná-la?\n\n"+
  "                ╰───────╮•╭───────╯\n\n")

#Decisao 1 -- SEGUIR VIAGEM
def historia_parte_1():
  # Criar raca
  print(
    "                ╭───────╯•╰───────╮\n\n" +
    "   Antes de iniciarmos, precisamos saber que tipo de criatura você é.\n\n" +
    "   Cada uma das raças que habita Joyous Port veio de um lugar muito distante. Cada povo possui sua própria história, agora é sua vez de decidir qual você ajudará a escrever...\n\n"+
    "                ╰───────╮•╭───────╯\n\n"
  )

def historia_parte_2(raca):
  # Criar habilidade
  print(
    "                ╭───────╯•╰───────╮\n\n" +
    "   Muito bem, jovem " + raca + ". Você agora faz parte de uma tribo muito importante aqui em Joyous Port.\n\n" +
    "   Agora, resta-nos saber sua habilidade... Qual é o poder que está encoberto dentro de vós?\n\n" +
    "                ╰───────╮•╭───────╯\n\n"
  )

'''TODO'''
def historia_parte_3(raca, habilidade):
  # Perguntar o nome
  print(
    "                ╭───────╯•╰───────╮\n\n" +
    "   Hm...\n\n" +
    "   Interessante.\n\n" +
    "   A combinação de " + raca + " e " + habilidade + " é incrivelmente peculiar.\n\n" +
    "   Mas, ouça, jovem " + raca + ", antes de começarmos, sinto que falta algo importante! Ora, você ainda não informou como devo me referir a sua pessoa...\n\n" +
    "                ╰───────╮•╭───────╯\n\n"
  )

def historia_parte_4(personagem):
  print(
    "                ╭───────╯•╰───────╮\n\n" +
    "   " + personagem.nome + ", Joyous Port lhe deseja uma ótima viagem. Leve em sua sacola uma arma poderosa de sua escolha.\n\n"
    "                ╰───────╮•╭───────╯\n\n"
  )

def historia_parte_5(personagem):
  print(
    "                ╭───────╯•╰───────╮\n\n" +
    "   Sábia escolha!\n\n" +
    "   Sua sacola de itens se encontra assim:\n\n" +
    "   ╔══════════════════════════◊══════════════════════════╗\n\n" +
    "   " + personagem.sacola[0].upper() + " | " +
            personagem.sacola[1].upper() + " | " +
            personagem.sacola[2].upper() + " | " +
            personagem.sacola[3].upper() + " \n\n" +
    "   CAPACIDADE (" + str(len(personagem.sacola)) + "/4)\n\n" +
    "   ╚══════════════════════════◊══════════════════════════╝\n\n" +
    "   Certo. Vamos seguir viagem. Há muito a ser feito. Enquanto caminhamos, vou lhe contar uma lenda muito famosa no sul do continente...\n\n" +
    "   Há muitos anos, durante a Era do Fogo, os povos viviam em harmonia. Porém, tudo mudou à medida que diversas aldeias começaram a seguir o pequeno - porém convincente - minotauro Berlúcio. Berlúcio se alimentava de fogo e solicitava que lhe entregassem seus poderes para que ele pudesse continuar disseminando suas palavras por toda a ilha.\n\n" +
    "   Porém, isso não era suficiente. Um certo dia, Berlúcio solicitou aos seus seguidores que trouxessem magos e outros dominantes do fogo como um ato de sacrefício e adoração a ele. E assim se deu início à caça à magia. Joyous Port nunca mais foi a mesma.\n\n" +
    "   Muitos tentam derrotá-lo, mas precisam de toda ajuda possível, pois, a cada sacrefício, o minotauro se tornou maior e mais poderoso.\n\n" +
    "   Vejo que você já possui 1 " + personagem.sacola[3].lower() + ", mas isso não é o suficiente para derrotar uma criatura de fogo, não é mesmo? Por causa disso, lhe trouxe aqui, nesta floresta. Dizem que, quando os ataques começaram, magos e druidas dominantes dos elementos da água e do ar se uniram para criar um cristal poderoso, que seria capaz de dar poderes incríveis a armas, armaduras e acessórios.\n\n" +
    "   Vamos, " + personagem.nome.capitalize() + "! Procure este lendário cristal... É nossa única esperança de salvar o povoado.\n\n" +
    "                ╰───────╮•╭───────╯\n\n"
  )

def historia_parte_6(decisao):
  artigo = "na"
  regiao = ""
  if (decisao == "norte"):
    regiao = "Arena"
  elif (decisao == "sul"):
    artigo = "em"
    regiao = "Guayba Shore"
  elif (decisao == "leste"):
    artigo = "no"
    regiao = "Redemption Arc"
  else:
    regiao = "Gasometer Power Plant"

  print(
    "                ╭───────╯•╰───────╮\n\n" +
    "   Você caminha para a direção " + decisao + ". Algumas horas passam até você avistar algo que parece ser uma construção. Após dar mais uns dez passos, você chega " + artigo + " " + regiao + ".\n\n" +
    "   Uma onda gélida toma conta do local. Vasculhando, uma portinha secreta escondida no chão chama a sua atenção. Ao abri-la, você avista 𝓞 𝓛𝓮𝓷𝓭𝓪𝓻𝓲𝓸 𝓒𝓻𝓲𝓼𝓽𝓪𝓵.\n\n" +
    "                ╰───────╮•╭───────╯\n\n"
    )

def historia_parte_7(personagem, item_a_ser_removido):
  print(
    "                ╭───────╯•╰───────╮\n\n" +
    "   Você decidiu remover o item \'" + personagem.sacola[item_a_ser_removido] + "\' da sua sacola. Agora, você tem espaço sobrando e pode guardar o cristal.\n")
  # Adiciona cristal à sacola
  personagem.sacola.pop(item_a_ser_removido)
  personagem.sacola.append("𝓞 𝓛𝓮𝓷𝓭𝓪𝓻𝓲𝓸 𝓒𝓻𝓲𝓼𝓽𝓪𝓵")
  
  print("   Você olha para a sua bolsa e percebe que está uma bagunça! Você não será capaz de derrotar um minotauro sem, primeiramente, organizar sua vida.\n")

  personagem.sacola.sort()

  print(
  "   Pronto. Bem melhor...\n\n" +
  "   Sua sacola de itens se encontra assim:\n\n"+
  "   ╔══════════════════════════◊══════════════════════════╗\n\n" +
  "   " + personagem.sacola[0].upper() + " | " +
          personagem.sacola[1].upper() + " | " +
          personagem.sacola[2].upper() + " | " +
          personagem.sacola[3].upper() + " \n\n" +
  "   CAPACIDADE (" + str(len(personagem.sacola)) + "/4)\n\n" +
  "   ╚══════════════════════════◊══════════════════════════╝\n\n" +
  "   Ao fechar sua sacola e continuar sua jornada, você ouve uma voz:\n\n" +
  "   ɴᴜɴᴄᴀ ᴘᴇɴꜱᴇɪ Qᴜᴇ ꜱᴇʀɪᴀ ᴛᴀᴏ ꜰᴀᴄɪʟ ᴅᴇꜱᴛʀᴜɪʀ ᴏ ᴄʀɪꜱᴛᴀʟ. ᴠᴏᴄᴇ ɴᴀᴏ ᴛᴇᴍ ᴄʜᴀɴᴄᴇꜱ ᴄᴏɴᴛʀᴀ ᴍɪᴍ, ʜᴀʜᴀʜᴀʜᴀ.\n\n"
  "   Céus! É o minotauro! O que você irá fazer?\n\n" +
  "                ╰───────╮•╭───────╯\n\n"
  )
  return personagem

def historia_parte_8(personagem):
  print(
    "                ╭───────╯•╰───────╮\n\n" +
    "   Parabéns, " + personagem.nome + ". Você salvou nossa ilha. Joyous Port será eternamente grata por isso.\n\n" +
    "   Aqui está sua recompensa: 200 ɢᴏʟᴅ ᴘᴏɪɴᴛꜱ\n\n"
    "                ╰───────╮•╭───────╯\n\n")


#Decisao 1 -- SE HOSPEDAR NO HOTEL A LESTE DO VILAREJO E TIRAR UMAS FÉRIAS
def jogador_desistiu():
  print("   Vá pela sombra, jovem guerreiro. Lembre-se: seu destino não está traçado! Quem sabe nos encontremos novamente...")

#Decisao 1 -- IR PARA CASA JOGAR LOLZINHO
def jogador_desistiu_de_forma_ridicula():
  print("   Sério? Sério mesmo? Até mais, então.")
