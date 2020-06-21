# Bot configurations
BOT_TOKEN = '630034573:AAH2-LiPrG_KH_gE-EBEH8kadywuGRUUxAI'
BOT_NONE_STOP = True
AVAILABLE_COMMANDS = 'start', 'help'

# Owm configurations
OWM_TOKEN = '97962da4c6fd853621d3c05731b8a6f9'
OWM_LANG = 'en'


# Bot responses
START_TEXT = 'Hello! Send me the name of your city.'
HELP_TEXT = 'It\'s a weather bot. To get information about the weather in your city ' \
            'send me your city name on english language.'
UNKNOWN_COMMAND_TEXT = 'Unknown command "{command}".'
CITY_NOT_FOUND_TEXT = 'Sorry, city "{city}" is not found.'
WEATHER_INFO_TEXT = 'Weather in {city}:\n' \
                    'Temperature: {temperature} °C\n' \
                    'Wind: {wind} m/s\n' \
                    'Humidity: {humidity}%\n' \
                    'Pressure: {pressure} hPa\n' \
                    '{status}.'
