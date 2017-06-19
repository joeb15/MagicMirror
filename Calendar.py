import IO
import pygame as pg


def draw(x, y, w, h, display):
    events_data = IO.read("data/events")
    events = events_data.splitlines()
    for i in range(len(events)):
        event = events[i]
        if not event.__contains__(":"):
            break
        parts = event.split(":")
        days = parts[0]
        title = parts[1]
        if int(days) < 15:
            __draw_text(display, 25, (255, 255, 255), x, y + 30 * i, title)
            __draw_text(display, 25, (255, 255, 255), x + 400, y + 30 * i, days)


def __draw_text(display, size, color, x, y, text):
    font = pg.font.SysFont('times new roman', size)
    display.blit(font.render(text, 1, color), (x, y))