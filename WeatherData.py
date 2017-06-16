import requests
import IO


def get_data():
    page = requests.get("https://weather.com/weather/today/l/USCA0517:1:US").text
    __process_temp_and_weather(page)

    page = requests.get("http://www.accuweather.com/en/us/irvine-ca/92612/daily-weather-forecast/337095?day=1").text
    __process_precip(page)

    page = requests.get("https://weather.com/weather/tenday/l/USCA0517:1:US").text
    __process_other_days(page)

    page = requests.get("https://www.timeanddate.com/sun/usa/irvine").text
    __process_sunrise_sunset(page)


def __process_temp_and_weather(curr):
    parts = curr.split('<')
    i = 0
    for line in parts:
        if line.__contains__("today_nowcard-temp"):
            temp_stored = parts[i + 1].split(">")[1]
            IO.write("data/weather/temp", temp_stored)
        if line.__contains__("today_nowcard-phrase"):
            weather_stored = parts[i].split(">")[1]
            IO.write("data/weather/weather", weather_stored)
        i += 1


def __process_sunrise_sunset(curr):
    parts = curr.split(">")
    i = 0
    for line in parts:
        if line.__contains__("Sunrise Today:"):
            sunrise_stored = parts[i + 2].split("<")[0]
            IO.write("data/weather/sunrise", sunrise_stored)
        if line.__contains__("Sunset Today:"):
            sunset_stored = parts[i + 2].split("<")[0]
            IO.write("data/weather/sunset", sunset_stored)
        i += 1


def __process_other_days(curr):
    global days_stored
    days = curr.split("clickable closed")
    day = 0
    for part in days:
        if part.__contains__("date-time"):
            parts = part.split("<")
            i = 0
            for line in parts:
                if line.__contains__("date-time"):
                    dayotw = parts[i].split(">")[1]
                if line.__contains__("headers=\"hi-lo\""):
                    hi = parts[i + 2].split(">")[1]
                    lo = parts[i + 8].split(">")[1]
                if line.__contains__("headers=\"precip\""):
                    precip = parts[i + 5].split(">")[1]
                if line.__contains__("headers=\"wind\""):
                    wind = parts[i + 1].split(">")[1]
                if line.__contains__("headers=\"humidity\""):
                    humidity = parts[i + 2].split(">")[1]
                i += 1
            IO.write("data/weather/day" + repr(day) + "/dayotw", dayotw)
            IO.write("data/weather/day" + repr(day) + "/hi", hi)
            IO.write("data/weather/day" + repr(day) + "/lo", lo)
            IO.write("data/weather/day" + repr(day) + "/precip", precip)
            IO.write("data/weather/day" + repr(day) + "/wind", wind)
            IO.write("data/weather/day" + repr(day) + "/humidity", humidity)
            day += 1


def __process_precip(curr):
    global precip_stored
    parts = curr.split('>')
    for line in parts:
        if line.__contains__('Precipitation') and not line.__contains__(":"):
            precip_stored = line.split("<")[0].split(" ")[1].split("%")[0]
            IO.write("data/weather/precip", precip_stored)
