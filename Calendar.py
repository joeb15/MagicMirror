import pygame as pg

import IO


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
        if i < 7:
            if days == "0":
                days = "Today"
            elif days == "1":
                days = "Tomorrow"
            else:
                days = days + " days"
            col = 255 - i * i * 5
            __draw_text(display, 30, (col, col, col), x, y + 30 * i, title)
            __draw_text(display, 30, (col, col, col), x + 400 - sizeString(days, 25), y + 30 * i, days)


def sizeString(text, size):
    font = pg.font.SysFont('times new roman', size)
    text_image = font.render(str(text), False, (1, 1, 1))
    return text_image.get_width()


def __draw_text(display, size, color, x, y, text):
    font = pg.font.SysFont('times new roman', size)
    display.blit(font.render(text, 1, color), (x, y))