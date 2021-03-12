from tkinter import *


class Button:

    def __init__(self, canvas, pos_x, pos_y, width, height, text=None, font=None, anchor=None):

        if anchor == 'w':
            self.x = pos_x + width / 2
            self.y = pos_y
        elif anchor == 'e':
            self.x = pos_x - width / 2
            self.y = pos_y
        elif anchor == 'n':
            self.x = pos_x
            self.y = pos_y + height / 2
        elif anchor == 's':
            self.x = pos_x
            self.y = pos_y - height / 2
        elif anchor == 'nw':
            self.x = pos_x + width / 2
            self.y = pos_y + height / 2
        elif anchor == 'se':
            self.x = pos_x - width / 2
            self.y = pos_y - height / 2
        elif anchor == 'sw':
            self.x = pos_x + width / 2
            self.y = pos_y - height / 2
        elif anchor == 'ne':
            self.x = pos_x - width / 2
            self.y = pos_y + height / 2

        if text:
            self.text = text
        if font:
            self.font = font

        canvas.create_rectangle(self.x-width/2, self.y-height/2, self.x+width/2, self.y+height/2)
