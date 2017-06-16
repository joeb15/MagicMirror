import pygame as pg


def draw(x, y, w, h, display, message):
    __draw_text(display, 128, (255,255,255), 0, 0, message, w, h)


def __draw_text(display, size, color, x, y, text, width, height):
    font = pg.font.SysFont('times new roman', size)
    parts = text.split(" ")
    curr_line = ''
    line_array=[]
    width_array=[]
    new_line=''
    for curr in parts:
        new_line = curr_line+" "+curr
        str_size = sizeString(new_line, font)
        if str_size > width and not curr_line == '':
            line_array.append(curr_line)
            width_array.append(sizeString(curr_line, font))
            curr_line = curr
            new_line = curr
        else:
            curr_line=new_line
    line_array.append(new_line)
    width_array.append(sizeString(new_line, font))
    h = size*1.5*(len(line_array))
    for i in range(len(line_array)):
        display.blit(font.render(line_array[i], 1, color), (x+(width-width_array[i])/2, y-h/2+height/2-size*1.5*(len(line_array)-i-1)))


def sizeString(text, font):
    textimage = font.render(str(text), False, (1,1,1))
    return textimage.get_width()