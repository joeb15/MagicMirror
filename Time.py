import pygame as pg
import time

__months = ("January", "February", "March", "April", "May", "June", "July", "August", "September")
__days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")


def draw(x, y, w, h, display):
    date, time = getTime()
    __draw_text(display, 50, (255,255,255), x, y, date)
    __draw_text(display, 120, (255,255,255), x, y+50, time)


def __draw_text(display, size, color, x, y, text):
    font = pg.font.SysFont('times new roman', size)
    display.blit(font.render(text, 1, color), (x, y))


def getTime():
    tuple = time.localtime(time.time())
    date = __days[tuple[6]] + ", " + __months[tuple[1]] + " " + repr(tuple[2]) + ", " + repr(tuple[0])
    ampm="AM"
    hour = tuple[3]
    min = tuple[4]
    if min<10 :
        min = "0"+repr(min)
    else:
        min = repr(min)
    if hour>=12:
        hour -= 12
        ampm="PM"
    if hour == 0:
        hour = 12
    if hour<10 :
        hour = "0"+repr(hour)
    else:
        hour = repr(hour)
    timeHM = hour + ":" + min + " " + ampm
    return date, timeHM