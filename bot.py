import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

#Загружаем даные для ключа от FatherBot
import setting

logging.basicConfig(filename='bot.log', level=logging.INFO)

#Функция обработки события Start c двумя аргументамии (параметрами)
def greet_user(update, context):
  print('Вызван /start')

 #Производим взаимодйствие с пользователем
  update.message.reply_text('Привет, друг!')

def talk_to_me(update, context):
   text = update.message.text
   print(text)
   update.message.reply_text(text)


#Основная функция
def main():
    #Задаем параметры ключа для сервера и коннекта 
    mybot = Updater(setting.API_KEY, use_context=True)

    #Передаем переменой объект dispatcher
    dp = mybot.dispatcher

    #Задаем обработку события Start
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    #Информационное сообщение в лог
    logging.info("Бот стартовал")

    #Загрузка функций для работы бота
    mybot.start_polling()
    mybot.idle()

#Производим вызов процедуры по условию для правильного импорта
if __name__== '__main__':
 main()