import telebot
import time

from telebot.types import Message

bot = telebot.TeleBot("1906701890:AAE1V60meqDHUUDNtJSgsFR4ibb4x366ILE")

@bot.message_handler(commands=["start" ])
def start (mensaje):
    bot.send_chat_action (1500506100, 'typing')
    time.sleep(3) 
    bot.reply_to(mensaje, "Hola,Un gusto saludarte.")

@bot.message_handler(commands=["imagencuadratica"])
def imagencuadratica (mensaje):
    bot.send_chat_action(1500506100, 'formulacuadratica.jpg')
    time.sleep(3)
    bot.send_photo(1500506100, open('formulacuadratica.jpg', 'rb'),
    
@bot.message_handler(commands=["imagenformulasconversion"]) 
def imagenformulasconversion (mensaje):
    bot.send_chat_action (1500506100, 'typing')
    time.sleep(3) 
    bot.reply_to (mensaje, "Mi nombre es BotLagos. ¿En que puedo ayudarte?")

@bot.message_handler(commands=["documentopdf"]) 
def documentopdf (mensaje):
     bot.send_chat_action (1500506100, 'typing')
     time.sleep(3)
     bot.reply_to(mensaje, "Me siento joven y eso es lo importante")   

@bot.message_handler(commands=["ubicacionuniversidad"]) 
def ubicacionuniversidad (mensaje):
    bot.send_chat_action (1500506100, 'typing')
    time.sleep(3)
    bot.reply_to(mensaje, "No tengo una respuesta para eso .. Dime te puedo ayudar en otra cosa?")


bot.polling()