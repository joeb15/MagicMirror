import pygame as pg
import requests

person_stored = "Unknown"
quote_stored = "An apple a day keeps anyone away... If you throw it hard enough!"


def draw(x, y, w, h, display):
    __get_quote()
    __draw_text(display, 35, (255, 255, 255), 40, y + h - 50, quote_stored, 1000, True)
    # __draw_text(display, 35, (255, 255, 255), 40, y + h - 65, person_stored, 1000, True)


def __get_quote():
    global quote_stored, person_stored
    url = "https://www.brainyquote.com/quotes_of_the_day.html"
    page = requests.get(url).text
    pages = page.split("<")
    i = 0
    for line in pages:
        if line.__contains__('"qotd-h2">Quote of the Day'):
            quote_stored = pages[i + 4].split(">")[1].replace("&#39;","'")
            person_stored = pages[i + 6].split(">")[1]
        i += 1


def __draw_text(display, size, color, x, y, text, width=10000, center=False):
    font = pg.font.SysFont('times new roman', size)
    parts = text.split(" ")
    curr_line = ''
    line_array = []
    width_array = []
    new_line = ''
    for curr in parts:
        new_line = curr_line + " " + curr
        str_size = sizeString("__"+new_line+"__", font)
        if str_size > width and not curr_line == '':
            line_array.append(curr_line)
            width_array.append(sizeString(curr_line, font))
            curr_line = curr
            new_line = curr
        else:
            curr_line = new_line
    line_array.append(new_line)
    width_array.append(sizeString(new_line, font))
    if width != 10000:
        for i in range(len(line_array)):
            if center:
                display.blit(font.render(line_array[i], 1, color),
                             (x + (width - width_array[i]) / 2, y - size * 1.5 * (len(line_array) - i - 1)))
            else:
                display.blit(font.render(line_array[i], 1, color), (x, y - size * 1.5 * (len(line_array) - i - 1)))
        return x, y - size * 1.5 * (len(line_array) - 1), width, size * 1.5 * (len(line_array)), len(line_array)
    else:
        display.blit(font.render(text, 1, color), (x, y))


def sizeString(text, font):
    text_image = font.render(str(text), False, (1, 1, 1))
    return text_image.get_width()
