import telebot
from decouple import config
from telebot import types

bot = telebot.TeleBot(config("TOKEN_BOT"))


@bot.message_handler(commands=["start" , "hi"])
def get_start_message(message):
    full_name = f"{message.from_user.username}!!!"
    text = f"Welcome {full_name}"
    # bot.send_message(message.chat.id, text)
    bot.reply_to(message, text)



@bot.message_handler(content_types=["text"])
def get_message(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    if message.text.lower() == "меню":
       text = "выберите пожалуйста: чай или кофе"
       bot.send_message(message.chat.id, text)
       # btn1 = types.InlineKeyboardButton("Чай" ,url="https://en.wikipedia.org/wiki/Tea")
       btn1 = types.InlineKeyboardButton("Чай" , callback_data = "tea")
       btn2 = types.InlineKeyboardButton("кофе" , callback_data = "coffe")
       markup.add(btn1,btn2)
       bot.send_message(message.chat.id, text,reply_markup=markup)
@bot.callback_query_handler(func = lambda call : True)
def get_callback_data(call):
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if call.data == "tea":
        text = f"выберите желаемый чай"
        murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("black")
        btn2 = types.KeyboardButton("blue")
        btn3 = types.KeyboardButton("green")
        murkup.add(btn1,btn2,btn3)
    if  call.data == "coffe":
        text = f"выберите желаемый кофе "
        btn1 = types.KeyboardButton("latte")
        btn2 = types.KeyboardButton("cappuchino")
        btn3 = types.KeyboardButton("americano")
        murkup.add(btn1,btn2,btn3)
    bot.send_message(call.message.chat.id, text,reply_markup=murkup)







bot.polling()