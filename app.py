import os
import io
import telebot
from google.cloud import texttospeech
from pydub import AudioSegment
from telebot import types

API_TOKEN = 'TU API KEY DE TELEGRAM'

bot = telebot.TeleBot(API_TOKEN)

# Configuración del servicio de TTS de Google Cloud
client = texttospeech.TextToSpeechClient()

# Función para convertir texto a voz
def text_to_speech(text_input, voice_name):
    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(text=text_input)

    voice = texttospeech.VoiceSelectionParams(
        language_code=voice_name.split('-')[0] + '-us',
        name=voice_name
    )


    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        request={"input": input_text, "voice": voice, "audio_config": audio_config}
    )

    return response.audio_content





# Función para manejar el comando /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Español EE.UU. (F) - Neural2-A')
    itembtn2 = types.KeyboardButton('Español EE.UU. (M)- Neural2-B')
    itembtn3 = types.KeyboardButton('Español EE.UU. (M)- Neural2-C')
    itembtn4 = types.KeyboardButton('Español EE.UU. (M)- News-D')
    itembtn5 = types.KeyboardButton('Español EE.UU. (M)- News-E')
    itembtn6 = types.KeyboardButton('Español EE.UU. (F)- News-F')
    itembtn7 = types.KeyboardButton('Español EE.UU. (F)- News-G')
    itembtn8 = types.KeyboardButton('Español EE.UU. (F)- Standard-A')
    itembtn9 = types.KeyboardButton('Español EE.UU. (M)- Standard-B')
    itembtn10 = types.KeyboardButton('Español EE.UU. (M)- Standard-C')
    itembtn11 = types.KeyboardButton('Español EE.UU. (M)- Studio-B')
    itembtn12 = types.KeyboardButton('Español EE.UU. (F)- Wavenet-A')
    itembtn13 = types.KeyboardButton('Español EE.UU. (M)- Wavenet-B')
    itembtn14 = types.KeyboardButton('Español EE.UU. (M)- Wavenet-C')
    
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6, itembtn7, itembtn8, itembtn9, itembtn10, itembtn11, itembtn12, itembtn13, itembtn14)  # Agrega el quinto botón aquí
    msg = bot.send_message(message.chat.id, "Por favor, elige una de las siguientes voces:", reply_markup=markup)
    bot.register_next_step_handler(msg, process_language_choice)




# Función para manejar la elección de idioma
# Función para manejar la elección de idioma
def process_language_choice(message):
    language_choice = message.text
    if language_choice == 'Español EE.UU. (F) - Neural2-A':
        voice_name = 'es-US-Neural2-A'
    elif language_choice == 'Español EE.UU. (M)- Neural2-B':
        voice_name = 'es-US-Neural2-B'
    elif language_choice == 'Español EE.UU. (M)- Neural2-C':
        voice_name = 'es-US-Neural2-C'
    elif language_choice == 'Español EE.UU. (M)- News-D':
        voice_name = 'es-US-News-D'
    elif language_choice == 'Español EE.UU. (M)- News-E':
        voice_name = 'es-US-News-E'
    elif language_choice == 'Español EE.UU. (F)- News-F':
        voice_name = 'es-US-News-F'
    elif language_choice == 'Español EE.UU. (F)- News-G':
        voice_name = 'es-US-News-G'
    elif language_choice == 'Español EE.UU. (F)- Standard-A':
        voice_name = 'es-US-Standard-A'
    elif language_choice == 'Español EE.UU. (M)- Standard-B':
        voice_name = 'es-US-Standard-B'
    elif language_choice == 'Español EE.UU. (M)- Standard-C':
        voice_name = 'es-US-Standard-C'
    elif language_choice == 'Español EE.UU. (M)- Studio-B':
        voice_name = 'es-US-Studio-B'
    elif language_choice == 'Español EE.UU. (F)- Wavenet-A':
        voice_name = 'es-US-Wavenet-A'
    elif language_choice == 'Español EE.UU. (M)- Wavenet-B':
        voice_name = 'es-US-Wavenet-B'
    elif language_choice == 'Español EE.UU. (M)- Wavenet-C':
        voice_name = 'es-US-Wavenet-C'

    # Añade más opciones aquí, según las voces disponibles que desees utilizar
    else:
        bot.send_message(message.chat.id, "Lo siento, opción no válida.")
        return None, None
    msg = bot.send_message(message.chat.id, "Por favor ingresa el texto que deseas convertir a voz:")

    # Reemplaza la llamada original a bot.register_next_step_handler aquí
    if voice_name:
        bot.register_next_step_handler(msg, process_text_input, voice_name)


# Función para manejar el ingreso de texto y la conversión a voz
def process_text_input(message, voice_name):
    text_input = message.text
    audio_data = text_to_speech(text_input, voice_name)

    # Convertir el audio a mp3
    audio_segment = AudioSegment.from_file(io.BytesIO(audio_data))
    mp3_data = io.BytesIO()
    audio_segment.export(mp3_data, format='mp3')

    # Enviar el audio al usuario
    mp3_data.seek(0)
    bot.send_audio(message.chat.id, mp3_data)
    ask_continue(message)





def ask_continue(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Sí')
    itembtn2 = types.KeyboardButton('No')
    markup.add(itembtn1, itembtn2)
    msg = bot.send_message(message.chat.id, "¿Deseas convertir otro texto a voz?", reply_markup=markup)
    bot.register_next_step_handler(msg, process_continue_decision)



def process_continue_decision(message):
    continue_decision = message.text
    if continue_decision == 'Sí':
        send_welcome(message)
    elif continue_decision == 'No':
        bot.send_message(message.chat.id, "De acuerdo, si deseas convertir otro texto a voz más tarde, simplemente utiliza el comando /start.")
    else:
        bot.send_message(message.chat.id, "Lo siento, opción no válida.")
        ask_continue(message)


# Iniciar el bot
bot.polling()


#bot creado por David Vega DaveNISC , para mas informacion visita www.davenisc.com o al correo dave@davenisc.com



