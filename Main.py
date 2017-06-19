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


def split():
    global p
    p = Process(target=get_data)
    p.start()


def get_data():
    while IO.exists("data/running"):
        WeatherData.get_data()
        CalendarData.get_data()


def main():
    IO.create("data/running")
    pg.init()
    split()
    display = pg.display.set_mode((1080, 1920), NOFRAME)
    while IO.exists("data/running"):
        for event in pg.event.get():
            if event.type==QUIT:
                IO.delete("data/running")
            elif event.type == KEYDOWN:
                if event.key == K_MINUS:
                    display = pg.display.set_mode((1080, 1920), NOFRAME)
                if event.key == K_EQUALS:
                    display = pg.display.set_mode((1080, 1920))
        display.fill((0, 0, 0))
        Calendar.draw(0, 250, 700, 700, display)
        DisplayMessage.draw(0,0,1080,1920,display,"Hello, Joe")
        Weather.draw(700, 0, 380, 600, display)
        Time.draw(0, 0, 400, 600, display)
        DailyQuote.draw(0, 1920-200, 200, 200, display)
        pg.display.update()
    p.join()
    pg.quit()


main()