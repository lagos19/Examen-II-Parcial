import time
import telebot
from telebot import types

TOKEN = '1906701890:AAE1V60meqDHUUDNtJSgsFR4ibb4x366ILE'

knownUsers = [] 
userStep = {}  

commands = { 
    'start'         : 'Iniciar el bot\n\n',
    'examen'        : 'Mostrar examen'
}

imageSelect = types.ReplyKeyboardMarkup(one_time_keyboard=True)  
imageSelect.add('Imagen Formula Cuadratica', 'Imagen Conversion Unidades','Documento PDF','Ubicacion Universidad')

hideBoard = types.ReplyKeyboardRemove()  

def get_user_step(uid):
    if uid in userStep:
        return userStep[uid]
    else:
        knownUsers.append(uid)
        userStep[uid] = 0
        print("Nuevo usuarios detectado, pero no ha usado \"/start\" ")
        return 0

def listener(messages):
    for m in messages:
        if m.content_type == 'text':0
    print(str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text)

bot = telebot.TeleBot(TOKEN)
bot.set_update_listener(listener)     

@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    if cid not in knownUsers: 
        knownUsers.append(cid)  
        userStep[cid] = 0 
        
        bot.send_message(cid, 'Bienvenido')
        bot.send_chat_action(cid, 'typing')  
        time.sleep(1)
        bot.send_chat_action(cid, 'typing')  
        time.sleep(1)
        command_help(m) 
    else:
        bot.send_message(cid, "Ya usaste el comando /start, usa el comando /help para visualizar más comandos")

@bot.message_handler(commands=['help'])
def command_help(m):
    cid = m.chat.id
    help_text = "Incio de BotExamen:\n\n\n"
    for key in commands: 
            help_text += "/" + key + ": "
            help_text += commands[key] + "\n"
    bot.send_message(cid, help_text)  

@bot.message_handler(commands=['examen'])
def command_image(m):
    cid = m.chat.id
    bot.send_message(cid, "Selecciona la tecla de tu preferencia ", reply_markup=imageSelect)  
    userStep[cid] = 1 

@bot.message_handler(func=lambda message: get_user_step(message.chat.id) == 1)
def msg_image_select(m):
    cid = m.chat.id
    text = m.text
    bot.send_chat_action(cid, 'typing')
    time.sleep(1)
    bot.send_chat_action(cid, 'typing')
    time.sleep(1)
    bot.send_chat_action(cid, 'typing')
    time.sleep(1)

    if text == 'Imagen Formula Cuadratica':
        bot.send_message(cid, "A continuacíon se muestra imagen de la formula cuadratica")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('formulacuadratica.jpg', 'rb'),
                       reply_markup=hideBoard)  
        time.sleep(3)
        bot.send_message(cid, "Selecciona el comando /examen para realizar otra consulta ")
        userStep[cid] = 0 

    elif text == 'Imagen Conversion Unidades':
        bot.send_message(cid, "A continuacíon se muestra imagen de la Conversion Unidades")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_chat_action(cid, 'upload_photo')
        time.sleep(3)   
        bot.send_photo(cid, open('formuladeconversion.jpg','rb'),
                       reply_markup=hideBoard)  
        time.sleep(3)
        bot.send_message(cid, "Selecciona el comando /examen para realizar otra consulta")
        userStep[cid] = 0  

    elif text == 'Documento PDF':
        bot.send_message(cid, "A continuacíon se  muetra Documento PDF")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_chat_action(cid, 'upload_document')
        time.sleep(3)   
        bot.send_document(cid, open('valor.pdf','rb'),
                       reply_markup=hideBoard)  
        time.sleep(3)
        bot.send_message(cid, "Selecciona el comando /examen para realizar otra consulta")
        userStep[cid] = 0

    elif text == 'Ubicacion Universidad':
        bot.send_message(cid, "A continuacíon se muestra la ubicacion de la Ubicacion Universidad")
        bot.send_chat_action(cid, 'typing')
        time.sleep(3)
        bot.send_chat_action(cid, 'find_location')
        time.sleep(3)   
        bot.send_location(cid, latitude=15.495804194472132,longitude=-87.99127844006198,
                       reply_markup=hideBoard)  
        time.sleep(3)
        bot.send_message(cid, "Selecciona el comando /examen para realizar otra consulta")
        userStep[cid] = 0   
    else:
        bot.send_message(m.chat.id, "No entiendo el texto:\"" + m.text + "\"\nIntenta usar /help para visualizar la lista de comandos disponibles")
        bot.send_message(cid, "Vamos, intentalo de nuevo. ")

bot.polling()