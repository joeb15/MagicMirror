import pygame as pg
import requests

dariella_torres = pg.image.load("images/horse.png")
person_stored = "Unknown"
quote_stored = "An apple a day keeps anyone away... If you throw it hard enough!"


def draw(x, y, w, h, display):
    pg.draw.rect(display, (255, 255, 255), (x, y, w, h))
    __get_quote()
    __draw_quote_bubble(display, x, y, w, h)
    __draw_text(display, 35, (255, 255, 255), x + w + 100, y+h - 125, quote_stored, 750, True)
    __draw_text(display, 35, (255, 255, 255), x + w + 100, y + h - 75, person_stored, 750, True)
    display.blit(dariella_torres, (x, y, w, h))


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


def __draw_quote_bubble(display, x, y, w, h):
    thickness=10
    corner_size=25

    l, t, w2, h2, length = __draw_text(display, 35, (255, 255, 255), x + w + 100, y + h - 125, quote_stored, 750, True)
    h2 = h2 * (length + 1) / length
    l-=thickness
    t-=thickness
    w2+=2*thickness
    h2+=2*thickness

    """main rect"""
    pg.draw.rect(display, (255, 255, 255), (l, t, w2, h2))
    pg.draw.rect(display, (0, 0, 0), (l + thickness, t + thickness, w2 - 2*thickness, h2 - 2*thickness))

    """to horse part"""
    pg.draw.rect(display, (0, 0, 0), (l, t + h2 / 2 - corner_size, thickness, corner_size * 2))
    pg.draw.circle(display, (255, 255, 255), (int(l - corner_size), int(t + h2 / 2 - corner_size)),
                   corner_size + thickness)
    pg.draw.circle(display, (255, 255, 255), (int(l - corner_size), int(t + h2 / 2 + corner_size)),
                   corner_size + thickness)
    pg.draw.circle(display, (0, 0, 0), (int(l - corner_size), int(t + h2 / 2 - corner_size)), corner_size)
    pg.draw.circle(display, (0, 0, 0), (int(l - corner_size), int(t + h2 / 2 + corner_size)), corner_size)
    pg.draw.rect(display, (0, 0, 0), (
    l - 2 * corner_size - thickness, t + h2 / 2 - corner_size * 2 - thickness, corner_size * 2 + thickness,
    corner_size + thickness))
    pg.draw.rect(display, (0, 0, 0), (
    l - 2 * corner_size - thickness, t + h2 / 2 + corner_size, corner_size * 2 + thickness, corner_size + thickness))
    pg.draw.rect(display, (0, 0, 0), (
    l - 2 * corner_size - thickness, t + h2 / 2 - corner_size * 2 - thickness, corner_size + thickness,
    4 * corner_size + 2 * thickness))

    """top left corner"""
    pg.draw.rect(display, (0, 0, 0), (l, t, corner_size, corner_size))
    pg.draw.circle(display, (255, 255, 255), (int(l + corner_size), int(t + corner_size)), corner_size)
    pg.draw.circle(display, (0, 0, 0), (int(l + corner_size), int(t + corner_size)), corner_size-thickness)
    pg.draw.rect(display, (0, 0, 0), (l + corner_size, t + thickness, 2*corner_size, 2*corner_size))
    pg.draw.rect(display, (0, 0, 0), (l + thickness, t + corner_size, 2*corner_size, 2*corner_size))

    """top right corner"""
    pg.draw.rect(display, (0, 0, 0), (l + w2 - corner_size, t, corner_size, corner_size))
    pg.draw.circle(display, (255, 255, 255), (int(l + w2 - corner_size), int(t + corner_size)), corner_size)
    pg.draw.circle(display, (0, 0, 0), (int(l + w2 - corner_size), int(t + corner_size)), corner_size-thickness)
    pg.draw.rect(display, (0, 0, 0), (l + w2 - 3*corner_size, t + thickness, 2*corner_size, 2*corner_size))
    pg.draw.rect(display, (0, 0, 0), (l + w2 - 2*corner_size-thickness, t + corner_size, 2*corner_size, 2*corner_size))

    """bottom right corner"""
    pg.draw.rect(display, (0, 0, 0), (l + w2 - corner_size, t + h2 - corner_size, corner_size, corner_size))
    pg.draw.circle(display, (255, 255, 255), (int(l + w2 - corner_size), int(t + h2 - corner_size)), corner_size)
    pg.draw.circle(display, (0, 0, 0), (int(l + w2 - corner_size), int(t + h2 - corner_size)), corner_size-thickness)
    pg.draw.rect(display, (0, 0, 0), (l + w2 - 3*corner_size, t + h2 - 2*corner_size-thickness, corner_size*2, corner_size*2))
    pg.draw.rect(display, (0, 0, 0), (l + w2 - 2*corner_size-thickness, t + h2 - 3*corner_size, corner_size*2, corner_size*2))

    """bottom left corner"""
    pg.draw.rect(display, (0, 0, 0), (l, t + h2 - corner_size, corner_size, corner_size))
    pg.draw.circle(display, (255, 255, 255), (int(l+corner_size), int(t + h2 - corner_size)), corner_size)
    pg.draw.circle(display, (0, 0, 0), (int(l+corner_size), int(t + h2 - corner_size)), corner_size - thickness)
    pg.draw.rect(display, (0, 0, 0), (l + corner_size, t + h2 - 2 * corner_size - thickness, corner_size * 2, corner_size * 2))
    pg.draw.rect(display, (0, 0, 0), (l + thickness, t + h2 - 3 * corner_size, corner_size * 2, corner_size * 2))

    """
    pg.draw.rect(display, (0, 0, 0), (l - corner_size+thickness, t + h2/2 - corner_size, corner_size, corner_size))
    pg.draw.circle(display, (255, 255, 255), (int(l - corner_size), int(t + h2/2 - corner_size)), corner_size+thickness)
    pg.draw.circle(display, (0, 0, 0), (int(l - corner_size), int(t + h2/2 - corner_size)), corner_size)
    pg.draw.rect(display, (0, 0, 0), (l - 3*corner_size+thickness, t + h2/2 - 2*corner_size-thickness, corner_size*2, corner_size*2))
    pg.draw.rect(display, (0, 0, 0), (l - 2*corner_size, t + h2/2 - 3*corner_size, corner_size*2, corner_size*2))
    pg.draw.rect(display, (0, 0, 0), (int(l - corner_size), int(t + h2/2), corner_size+thickness, thickness))
    """


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
