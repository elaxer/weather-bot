import consts
import pyowm
import telebot
from time import sleep
from functions import is_undefined_command, get_details_about_weather

# Init bot and owm objects
bot = telebot.TeleBot(consts.BOT_TOKEN)
owm = pyowm.OWM(consts.OWM_TOKEN, language=consts.OWM_LANG)


@bot.message_handler(func=is_undefined_command)
def undefined_commands_handler(message):
    """Handler for undefined commands"""
    bot.send_message(
        message.chat.id,
        consts.UNKNOWN_COMMAND_TEXT.format(command=message.text)
    )


@bot.message_handler(commands=consts.AVAILABLE_COMMANDS)
def commands_handler(message):
    """Handler for defined commands"""
    if message.text == '/start':
        bot.send_message(message.chat.id, consts.START_TEXT)
    if message.text == '/help':
        bot.send_message(message.chat.id, consts.HELP_TEXT)


@bot.message_handler(content_types=('text',))
def city_handler(message):
    """Handles city name and returns details of weather in city"""
    try:
        # Formats city name
        city_name = message.text.lower().capitalize()

        # Gets details of weather. Can throw error if city name not found
        temperature, wind, humidity, pressure, status = get_details_about_weather(
            owm, city_name
        )

        text = consts.WEATHER_INFO_TEXT.format(
            city=city_name, temperature=temperature,
            wind=wind, humidity=humidity,
            pressure=pressure, status=status
        )
        print('Got message from {user_id}: {message}'.format(user_id=message.chat.id, message=message.text))
        bot.send_message(message.chat.id, text)
        print('Send message for user {user_id}: {message}\n'.format(user_id=message.chat.id, message=text))
    except pyowm.exceptions.api_response_error.APIResponseError:
        # If input city name not found
        bot.send_message(message.chat.id, consts.CITY_NOT_FOUND_TEXT.format(city=city_name))


if __name__ == '__main__':
    try:
        bot.infinity_polling()
    except Exception as e:
        print('Error! ' + e)
