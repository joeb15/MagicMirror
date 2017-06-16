# -*- coding: utf-8 -*-

import pygame as pg, IO

rain_small = pg.transform.scale(pg.image.load("images/raindrop.png"), (30,30))
sun_small = pg.transform.scale(pg.image.load("images/sunny.png"), (30,30))

weather_image_scale=(150,150)
sunny = pg.transform.scale(pg.image.load("images/sunny.png"), weather_image_scale)
cloudy = pg.transform.scale(pg.image.load("images/cloudy.png"), weather_image_scale)
rainy = pg.transform.scale(pg.image.load("images/rainy.png"), weather_image_scale)
unknown = pg.transform.scale(pg.image.load("images/horse.png"), weather_image_scale)
raindrop = pg.transform.scale(pg.image.load("images/raindrop.png"), (50,50))
wind = pg.transform.scale(pg.image.load("images/wind.png"), (40,40))


def draw(x, y, w, h, display):
    weather_stored = IO.read("data/weather/weather")
    precip_stored =  IO.read("data/weather/precip")
    temp_stored = IO.read("data/weather/temp")
    temperature = u'°'
    __draw_text(display, 250, (255, 255, 255), x, y, temp_stored + temperature)

    if weather_stored.__contains__("Fair") or weather_stored.__contains__("Sun"):
        weather_image=sunny
    elif weather_stored.__contains__("Cloud"):
        weather_image=cloudy
    elif weather_stored.__contains__("Rain"):
        weather_image=rainy
    else:
        weather_image=unknown
    display.blit(weather_image, (x-150, y))
    display.blit(raindrop, (x-50, y+130))
    curr_precip = precip_stored + "%"
    __draw_text(display, 40, (255, 255, 255), x-50-sizeString(curr_precip, 40), y + 135, curr_precip)
    if IO.exists("data/weather/day0/wind"):
        curr_wind = IO.read("data/weather/day0/wind").split(" ", 1)[1]
        __draw_text(display, 25, (255, 255, 255), x-50-sizeString(curr_wind, 25), y + 180, curr_wind)
    display.blit(wind, (x-50, y+180))
    """40x40"""

    yPos = 250
    space = 30
    for i in range(1, 7):
        curr_day = "data/weather/day" + repr(i)+"/"
        if not IO.exists(curr_day):
            break;
        col_val = 255-6*(i-1)*(i-1)
        col=(col_val,col_val,col_val)
        __draw_text(display, 30, col, x + 140, y + yPos + space * i, IO.read(curr_day + "dayotw"))
        if IO.read(curr_day+ "precip")== "0":
            sun_small.set_alpha(col_val)
            display.blit(sun_small, (x+210, y+yPos+space*i))
            sun_small.set_alpha(255)
        else:
            rain_small.set_alpha(col_val)
            display.blit(rain_small, (x+210, y+yPos+space*i))
            rain_small.set_alpha(255)
        __draw_text(display, 30, col, x + 250, y + yPos + space * i, IO.read(curr_day + "lo") + " - " + IO.read(curr_day + "hi"))

    """
    __draw_text(display, 30, (255,255,255), x+260, y, sunrise_stored)
    __draw_text(display, 30, (255,255,255), x+260, y+30, sunset_stored)
    """


def __draw_text(display, size, color, x, y, text):
    font = pg.font.SysFont('times new roman', size)
    display.blit(font.render(text, 1, color), (x, y))


def sizeString(text, size):
    font = pg.font.SysFont('times new roman', size)
    text_image = font.render(str(text), False, (1, 1, 1))
    return text_image.get_width()
