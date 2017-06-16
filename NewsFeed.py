import pygame as pg
import time, IO

gradient = pg.transform.scale(pg.image.load("images/gradient.png"), (1080, 8*35))
prev_update=0
news_storage=[]


def draw(x, y, w, h, display):
    global prev_update, news_storage
    t1=time.time()/15
    t = int(t1)
    t2 = t1%1

    """UPDATE NEWS EVERY 120 SECONDS"""
    update_news = repr(int(t1*15/120))
    if update_news != prev_update:
        IO.create("data/update_news")
        prev_update=update_news
    if IO.exists("data/news_done"):
        news_storage = IO.read("data/news").splitlines()
        IO.delete("data/news_done")
    for i in range(len(news_storage)):
        num=(i+t)%len(news_storage)
        if i >= 9:
            break
        x_split = (i-t2-3.5)*1.5

        __draw_text(display, 25, (255,255,255), x+49-x_split*x_split, y+(i-t2)*35, news_storage[num])
    pg.draw.rect(display, (0,0,0), (x, y+8*35, w, 35))
    pg.draw.rect(display, (0,0,0), (x, y-35, w, 35))
    display.blit(gradient, (x, y))


def __draw_text(display, size, color, x, y, text):
    font = pg.font.SysFont('times new roman', size)
    display.blit(font.render(text, 1, color), (x, y))
