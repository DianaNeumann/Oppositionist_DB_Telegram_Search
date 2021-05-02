import telebot


TGBOT_TOKEN = 'ваш токен'
TGBOT_CHAT_ID = 'ваш айди'

bot = telebot.TeleBot(TGBOT_TOKEN, parse_mode=None)


f = open('navalny.txt').readlines()

@bot.message_handler(content_types=['text', 'document', 'audio'])
def send_welcome(message):
    if message.text == "/start":
        f_input = bot.send_message(message.from_user.id, "Введите почту: ")

        bot.register_next_step_handler(f_input, find_str)
    else:

        bot.send_message(message.from_user.id,"Привет! Тут ты можешь узнать, есть ли твоя почта в базе free.navalny.ru! \n\nЧтобы начать, напиши /start .")
    
def find_str(message):
    if message.text != ' ' or '':
        for i in f:
            s = i.find(message.text)
            if s != -1:
                bot.send_message(message.from_user.id, str(i))
            
    bot.send_message(message.from_user.id, "--\nЭто всё, что удалось найти.")


    
bot.polling(none_stop=True, interval=0)
