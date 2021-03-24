from Apps.contrib.control import *
from tkinter.font import Font


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


class Tablica:

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.x = 0
        self.y = 0

    def addsym(self, symbol, canvas):
        value = GetMemoryField('table')
        value[self.y][self.x] += symbol
        canvas.create_rectangle(960-750+100*self.x, 500+100*self.y, 960-650+100*self.x, 600+100*self.y, fill='white')
        SetMemoryField('table', value=value)
        canvas.create_text(960-745+100*self.x, 550+100*self.y, text=GetMemoryField('table')[self.y][self.x], font='JetBrainsMono 25', anchor='w')
        self.Middle(canvas)

    def createcursor(self, canvas):
        try:
            canvas.delete(self.cursor)
        except:
            pass
        text = GetMemoryField('table')[self.y][self.x]
        size = Font(font='JetBrainsMono 25').measure(text=text)
        self.cursor = canvas.create_line(960-743+100*self.x+size, 650-100+100*self.y-22, 960-743+100*self.x+size, 650-100+100*self.y+22)

    def keyboard(self, keysym, canvas=None):

        if keysym == "Right":
            if self.x < self.width-1:
                self.x += 1
            else:
                self.x = 0

        elif keysym == "Left":
            if self.x > 0:
                self.x -= 1
            else:
                self.x = self.width-1

        elif keysym == "Down":
            if self.y < self.height-1:
                self.y += 1
            else:
                self.y = 0

        elif keysym == "Up":
            if self.y > 0:
                self.y -= 1
            else:
                self.y = self.height-1

        elif keysym == "BackSpace":
            value = GetMemoryField('table')
            value[self.y][self.x] = value[self.y][self.x][:-1]
            SetMemoryField('table', value=value)
            canvas.create_rectangle(960-750+100*self.x, 500+100*self.y, 960-650+100*self.x, 600+100*self.y, fill='white')
            canvas.create_text(960-745+100*self.x, 550+100*self.y, text=GetMemoryField('table')[self.y][self.x], font='JetBrainsMono 25', anchor='w')
            self.Middle(canvas)

    def Middle(self, canvas):
        Memory = GetMemoryField('table')
        for y in range(5):
            Counter = 0
            Number = 0
            for x in range(10):
                if not (Memory[y][x] == '' or Memory[y][x] == '.'):
                    Counter += float(Memory[y][x])
                    Number += 1
            canvas.create_rectangle(960 + 250, 500 + 100 * y, 960 + 400, 600 + 100 * y, fill='white')
            if Number > 0:
                Counter = Counter / Number
                Memory[y][10] = round(Counter, 1)
            else:
                Memory[y][10] = ''
            canvas.create_text(960+260, 550+100*y, text=Memory[y][10], font='JetBrainsMono 25', anchor='w')
        SetMemoryField('table', Memory)
