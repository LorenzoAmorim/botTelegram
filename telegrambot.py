import telebot

# chave api, do administrador do bot
CHAVE_API = "bot_api"

# defini o bot de fato aqui
bot = telebot.TeleBot(CHAVE_API)

#############################################################

@bot.message_handler(commands=["opção1"])
def opcao1 (mensagem):
    pass

@bot.message_handler(commands=["opção2"])
def opcao2 (mensagem):
    bot.reply_to(mensagem, "Fiz uma promessa pra mim mesmo, nunca mais comer torresmo, alguém me disse outro dia que para sentir satisfação e alegria é necessário ser caridoso, me dá um reaaaaaaaau, me dá um real ae onnnnnnnh cavnheauuuu nheuumenheumhaaai , o que fazer se não fazer, e aceitar o tédio enfadonho, então acho a receita encaminha, na caminhada, e subindo o moro, penso na sensação agradável, de vir mais rápido na descida pois estou numa baaaiiiiikiiiiiiiii, corro o risco de tropeçar em mim mesmo e cair quebrando o pescoço, pescoço em francês é âââânuuss, ânus, é a parte aboral do corpo, vivendo e aprendendo, o que o gato disse para o leite antes de bebe-lo, miaaaaaau, não procure saber onde vooou, meu caminho é toda manhãã, você gosta de maçã? Eu também, mas não têm. Aleluia, aleluia, aleluia, reze uma ava av Ave Maria, um pai nosso e um glória o pai, e assim você deverá ser feliz, ser feliz, a felicidade não está no PIco da montanha, está enquanto você escala esta montanha.")
    pass

@bot.message_handler(commands=["opção3"])
def opcao3 (mensagem):
    pass





# cria uma função para verificar qual a mensagem o bot vai dizer
def verificar(mensagem):
    return True

#decorator
# pega as infos das mensagens que estão sendo recebidas e basicamente programa quando deve a mensagem deve ser executada
"""@bot.message_handler(func=verificar)"""
# define função que responde a qualquer mensagem e obviamente leva como parâmetro uma mensagem
"""def responder(mensagem):
    bot.reply_to(mensagem, "Eai, aqui é o bot do L!!!!!")"""

@bot.message_handler(func=verificar)
def opcoes (mensagem):
    texto = """
/opção1 nada (surpresa)
/opção2 nada kkkk (surpresa 2)
/opção3 nada KKKKKKKKKK (surpresa 3)
    """
    bot.reply_to(mensagem, texto)


# basicamente um loop infinito do bot, para que enquanto houver uma conversa com ele, ele não pare e
# armazene as msgs e da respostas e etc.
bot.polling()