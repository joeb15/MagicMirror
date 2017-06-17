import pygame as pg, IO


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
        __draw_text(display, 25, (255,255,255), x, y+30*i, days + "|" + title)
    print("done")


def __draw_text(display, size, color, x, y, text):
    font = pg.font.SysFont('times new roman', size)
    display.blit(font.render(text, 1, color), (x, y))