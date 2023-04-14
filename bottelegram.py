import telebot


CHAVE_API = "6258912469:AAHhZEnx8-dxlZ6dYrTZSTfioBV7vpYPUJw"

bot = telebot.TeleBot(CHAVE_API)

def verificar(mensagem):
    return True



@bot.message_handler(commands=["opcao1"])

def opcao1(mensagem):
    bot.reply_to(mensagem, """Escolha uma opção para continuar (Clique no item):

BENEFÍCIOS DE SER VIP!
️LISTA ORGANIZADA
️ORDEM ALFABÉTICA
️BUSCA POR HASHTAG
️VIDEOS AMADORES
️PACKS EXCLUSIVAS
️MAIS DE 10MIL MÍDIAS/400 MÍDIAS DIÁRIAS ATÉ MAIS
️VAZADOS INÉDITOS EM PRIMEIRA MÃO 
  +
VALOR DO VIP➡️POR APENAS R$ 14,99 ISSO MESMO (14,99)

PIX E-MAIL :
brmendesbraz123@gmail.com
 Após o efetuamento do pagamento,envia o print para>> @capitaoadm 

ACESSO IMEDIATO,Pagou ? Entrou na hora,Sem enrolação e sem frescuras…

✅✅✅
""")


@bot.message_handler(commands=["opcao2"])

def opcao2(mensagem):
    bot.reply_to(mensagem, """Escolha uma opção para continuar (Clique no item):

BENEFÍCIOS DE SER VIP!
️LISTA ORGANIZADA
️ORDEM ALFABÉTICA
️BUSCA POR HASHTAG
️VIDEOS AMADORES
️PACKS EXCLUSIVAS
️MAIS DE 80MIL MÍDIAS/500 MÍDIAS DIÁRIAS ATÉ MAIS
️VAZADOS INÉDITOS EM PRIMEIRA MÃO 
  +
VALOR DO VIP➡️POR APENAS R$ 150,00 ISSO MESMO (150,00)

PIX E-MAIL :
brmendesbraz123@gmail.com
 Após o efetuamento do pagamento,envia o print para>> @capitaoadm 

ACESSO IMEDIATO,Pagou ? Entrou na hora,Sem enrolação e sem frescuras…

✅✅✅""")



@bot.message_handler(func=verificar)

def responder(mensagem):
    texto = """Escolha uma opção para continuar
(Clique na opção)
/opcao1 Vip 1 Mês 
/opcao2 Vip 1 ano
Responder qualquer outra coisa não vai funcionar clique em uma das opções"""


    bot.reply_to(mensagem, texto)

bot.polling()
