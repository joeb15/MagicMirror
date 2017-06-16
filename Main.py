import pygame as pg
import IO, Weather, Time, DailyQuote, DisplayMessage, NewsFeed, WeatherData, NewsData
from multiprocessing import Process
from pygame.locals import *


def split():
    global p
    p = Process(target=get_data)
    p.start()


def get_data():
    while IO.exists("data/running"):
        WeatherData.get_data()
        NewsData.get_data()


def main():
    IO.create("data/running")
    running=True
    pg.init()
    split()
    display = pg.display.set_mode((1080,1920))
    while running:
        for event in pg.event.get():
            if event.type==QUIT:
                running=False
                IO.delete("data/running")
            elif event.type == KEYDOWN:
                if event.key == K_MINUS:
                    display = pg.display.set_mode((1080, 1920), NOFRAME)
                if event.key == K_EQUALS:
                    display = pg.display.set_mode((1080, 1920))
        if running:
            display.fill((0, 0, 0))
            NewsFeed.draw(0,250,700,500,display)
            DisplayMessage.draw(0,0,1080,1920,display,"Hello, Joe!")
            Weather.draw(700, 0, 380, 600, display)
            Time.draw(0, 0, 400, 600, display)
            DailyQuote.draw(0, 1920-200, 200, 200, display)
            pg.display.update()
    p.join()
    pg.quit()

main()
