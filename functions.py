import consts


def is_undefined_command(message):
    """Function to detect undefined input command"""
    return message.text[0] == '/' and message.text[1:] not in consts.AVAILABLE_COMMANDS


def get_details_about_weather(owm, city_name):
    """
    Returns tuple of information about weather in city
    :param owm: Object instance of OWM class
    :param city_name: Name of city
    :return: tuple of weather details
    """
    observation = owm.weather_at_place(city_name)
    weather = observation.get_weather()

    # Details of weather
    temperature = round(weather.get_temperature('celsius')['temp'])
    wind = weather.get_wind()['speed']
    humidity = weather.get_humidity()
    pressure = weather.get_pressure()['press']
    status = weather.get_detailed_status().capitalize()

    return temperature, wind, humidity, pressure, status
