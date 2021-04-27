from Apps.contrib.control import *
from tkinter.font import Font
from tkinter import Canvas
from math import *
from Apps.contrib.contrib import log


class Button:

    def __init__(self, canvas, pos_x, pos_y, width, height, anchor='c', **kwargs):

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

        self.text = kwargs.get('text', None)
        self.font = kwargs.get('font', None)
        self.color = kwargs.get('color', 'white')
        self.fontcolor = kwargs.get('fontcolor', 'black')

        self.width = width
        self.height = height

        canvas.create_rectangle(self.x-width/2, self.y-height/2, self.x+width/2, self.y+height/2, fill=self.color)
        canvas.create_text(self.x, self.y, text=self.text, font=self.font, fill=self.fontcolor)


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

        if self.page:
            if GetPage() == self.page:
                if self.event.x-self.width/2 < self.x < self.event.x+self.width/2 and self.event.y-self.height/2 < self.y < self.event.y+self.height/2:
                    return True
            else:
                return False
        else:
            if self.event.x - self.width / 2 < self.x < self.event.x + self.width / 2 and self.event.y - self.height / 2 < self.y < self.event.y + self.height / 2:
                return True
            else:
                return False


class Tablica:

    cursor: Canvas.create_line

    def __init__(self, width, height, canvas, memory='table'):
        self.width = width
        self.height = height
        self.memory = memory
        self.canvas = canvas

        self.x = 0
        self.y = 0

    def addsym(self, symbol, canvas):
        value = GetMemoryField(self.memory)
        value[self.y][self.x] += symbol
        canvas.create_rectangle(960-750+100*self.x, 500+100*self.y, 960-650+100*self.x, 600+100*self.y, fill='white')
        SetMemoryField(self.memory, value=value)
        canvas.create_text(960-745+100*self.x, 550+100*self.y, text=GetMemoryField(self.memory)[self.y][self.x], font='JetBrainsMono 25', anchor='w')
        self.handler()

    def createcursor(self, canvas):
        try:
            canvas.delete(self.cursor)
        except:
            pass
        text = GetMemoryField(self.memory)[self.y][self.x]
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
            value = GetMemoryField(self.memory)
            value[self.y][self.x] = value[self.y][self.x][:-1]
            SetMemoryField(self.memory, value=value)
            canvas.create_rectangle(960-750+100*self.x, 500+100*self.y, 960-650+100*self.x, 600+100*self.y, fill='white')
            canvas.create_text(960-745+100*self.x, 550+100*self.y, text=GetMemoryField(self.memory)[self.y][self.x], font='JetBrainsMono 25', anchor='w')
            self.handler()

    def Middle(self, canvas):
        Memory = GetMemoryField(self.memory)
        for y in range(self.height):
            Counter = 0
            Number = 0
            for x in range(self.width):
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
        SetMemoryField(self.memory, Memory)

    def handler(self):
        Memory = GetMemoryField(self.memory)

        def CheckLine(line: int):
            for x in range(0, self.width):
                if Memory[line][x] == '':
                    return False
            return True

        if self.memory == 'table':
            for y in range(0, self.height):
                if CheckLine(y):
                    self.Middle(self.canvas)

                    dS = 0
                    for x in range(self.width):
                        dS += pow(float(Memory[y][x]) - float(Memory[y][10]), 2)
                    dS = round((3 * sqrt(dS)) / 10, 1)

                    Memory[y][11] = str(dS)
                    Memory[y][12] = f'{Memory[y][10]}±{Memory[y][11]}'

                    if GetMemoryField('table-1')[0][12] != '':
                        tS = ((float(GetMemoryField('table-1')[0][12]) ** 2) * sin(radians(2 * 15 * (1 + y)))) / 9.8

                        Memory[y][13] = str(round(tS, 1))

            for y in range(self.height):
                for x in range(4):
                    self.canvas.create_rectangle(960+250+150*x, 500+100*y, 960+400+150*x, 600+100*y, fill='white')
                    if CheckLine(y):
                        self.canvas.create_text(960+255+150*x, 550+100*y, text=Memory[y][x+10], font='JetBrainsMono 25', anchor='w')

        elif self.memory == 'table-1':
            y = 0

            if CheckLine(0):
                self.Middle(self.canvas)

                dS = 0
                for x in range(self.width):
                    dS += pow(float(Memory[y][x]) - float(Memory[y][10]), 2)
                dS = round((3 * sqrt(dS)) / 10, 1)

                Memory[y][11] = str(dS)

                if GetMemoryField('h') != '' and GetMemoryField('h') != '0' and Memory[y][10] != '0':
                    V0 = float(Memory[y][10]) * sqrt(9.8 / (2 * int(GetMemoryField('h'))))
                    Memory[y][12] = str(round(V0, 1))

                    dV = float(Memory[y][11]) / float(Memory[y][10])
                    dV += int(GetMemoryField('error')[1]) / (2 * int(GetMemoryField('h')))
                    Memory[y][13] = str(round(dV, 1))

            for y in range(self.height):
                for x in range(4):
                    self.canvas.create_rectangle(960+250+150*x, 500+100*y, 960+400+150*x, 600+100*y, fill='white')
                    if CheckLine(y):
                        self.canvas.create_text(960+260+150*x, 550+100*y, text=Memory[y][x + 10], font='JetBrainsMono 25', anchor='w')

        SetMemoryField(self.memory, Memory)


class ErrorsTable:

    cursor: Canvas.create_line

    def __init__(self, height=2, memory='error'):
        self.height = height
        self.memory = memory

        self.y = 0

    def addsym(self, symbol, canvas):
        value = GetMemoryField(self.memory)
        value[self.y] += symbol
        canvas.create_rectangle(960, 410+150*self.y, 1660, 560+150*self.y, fill='white')
        SetMemoryField(self.memory, value=value)
        canvas.create_text(980, 485+150*self.y, text=GetMemoryField(self.memory)[self.y], font='JetBrainsMono 35', anchor='w')

    def createcursor(self, canvas):
        try:
            canvas.delete(self.cursor)
        except:
            pass
        text = GetMemoryField(self.memory)[self.y]
        size = Font(font='JetBrainsMono 35').measure(text=text)
        self.cursor = canvas.create_line(985+size, 440+150*self.y, 985+size, 530+150*self.y)

    def keyboard(self, keysym, canvas=None):
        if keysym == "Down":
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
            value = GetMemoryField(self.memory)
            value[self.y] = value[self.y][:-1]
            SetMemoryField(self.memory, value=value)
            canvas.create_rectangle(960, 410+150*self.y, 1660, 560+150*self.y, fill='white')
            canvas.create_text(980, 485+150*self.y, text=GetMemoryField(self.memory)[self.y], font='JetBrainsMono 35', anchor='w')


class HTable:

    cursor: Canvas.create_line

    def __init__(self, memory='h'):
        self.height = 1
        self.memory = memory

    def addsym(self, symbol, canvas):
        value = GetMemoryField(self.memory)
        value += symbol
        Button(canvas, 960, 800, 300, 100, anchor='n')
        SetMemoryField(self.memory, value=value)
        canvas.create_text(820, 850, text=GetMemoryField(self.memory), font='JetBrainsMono 25', anchor='w')

    def createcursor(self, canvas):
        try:
            canvas.delete(self.cursor)
        except:
            pass
        text = GetMemoryField(self.memory)
        size = Font(font='JetBrainsMono 25').measure(text=text)
        self.cursor = canvas.create_line(825+size, 850-35, 825+size, 850+35)

    def keyboard(self, keysym, canvas=None):
        if keysym == "BackSpace":
            value = GetMemoryField(self.memory)
            value = value[:-1]
            SetMemoryField(self.memory, value=value)
            Button(canvas, 960, 800, 300, 100, anchor='n')
            canvas.create_text(820, 850, text=GetMemoryField(self.memory), font='JetBrainsMono 25', anchor='w')
