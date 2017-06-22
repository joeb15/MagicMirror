import time
from multiprocessing import Process

import pygame as pg
from pygame.locals import *

import Calendar
import CalendarData
import DailyQuote
import DisplayMessage
import IO
import Time
import Weather
import WeatherData

path = ""


def split():
    global p
    p = Process(target=get_data)
    p.start()


def sleep(num):
    for i in range(num):
        if not IO.exists(path):
            break;
        time.sleep(4)


def get_data():
    while IO.exists(path):
        WeatherData.get_data()
        CalendarData.get_data()
        # sleep for 30 seconds @ 4 sec intervals making sure running exists
        sleep(15)


def main():
    global path
    if IO.exists("/home/pi/"):
        path = "/home/pi/MagicMirror/data/running"
    else:
        path = "MagicMirror/data/running"
    IO.create(path)
    pg.init()
    split()
    if path.__contains__("pi"):
        display = pg.display.set_mode((1080, 1920), FULLSCREEN)
    else:
        display = pg.display.set_mode((1080, 1920))
    while IO.exists(path):
        for event in pg.event.get():
            if event.type==QUIT:
                IO.delete(path)
            elif event.type == KEYDOWN:
                if event.key == K_MINUS:
                    display = pg.display.set_mode((1080, 1920), FULLSCREEN)
                if event.key == K_EQUALS:
                    display = pg.display.set_mode((100, 100))
                if event.key == K_LEFTBRACKET:
                    display = pg.display.set_mode((1080, 1920))
                if event.key == K_RIGHTBRACKET:
                    IO.delete(path)
        display.fill((0, 0, 0))
        Calendar.draw(0, 250, 700, 700, display)
        DisplayMessage.draw(0,0,1080,1920,display,"Hello, Joe")
        Weather.draw(700, 0, 380, 600, display)
        Time.draw(0, 0, 400, 600, display)
        DailyQuote.draw(0, 1920-200, 200, 200, display)
        pg.display.update()
        sleep(1)
    p.join()
    pg.quit()


main()