from Apps.contrib.control import GetPage


class Button:

    def __init__(self, canvas, pos_x, pos_y, width, height, text=None, font=None, anchor='c'):

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
        else:
            self.x = pos_x
            self.y = pos_y

        self.canvas = canvas

        self.text = text
        self.font = font

        self.width = width
        self.height = height

        canvas.create_rectangle(self.x-width/2, self.y-height/2, self.x+width/2, self.y+height/2)
        canvas.create_text(self.x, self.y, text=self.text, font=self.font)


class ButtonClick:

    def __init__(self, event, pos_x, pos_y, width, height, anchor='c', page=None):

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
        else:
            self.x = pos_x
            self.y = pos_y

        self.event = event
        self.page = page

        self.width = width
        self.height = height

    def check(self):

        if GetPage() == self.page:
            if self.event.x-self.width/2 < self.x < self.event.x+self.width/2 and self.event.y-self.height/2 < self.y < self.event.y+self.height/2:
                return True
        else:
            return False
