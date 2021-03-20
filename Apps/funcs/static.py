from Apps.contrib.control import SetPage
from Apps.contrib.classes import Button


def StartWindow(canvas):
    canvas.delete('all')
    SetPage(0)

    canvas.create_text(960, 540, text='Лабораторная работа', font='JetBrainsMono 50')


def Menu(canvas):
    canvas.delete('all')
    SetPage(1)

    canvas.create_text(960, 125, text='Меню', font='JetBrainsMono 70')

    buttons = ['Описание', 'Анимация', 'Погрешности', 'Таблица', 'График', 'Помощь', 'Завершить']
    x = 325
    for button in buttons:
        Button(canvas, 960, x, 400, 80, text=button, font='JetBrainsMono 30')
        x += 100

    Button(canvas, 1900, 20, 150, 50, text='Сохранения', font='JetBrainsMono 15', anchor='ne')


def Description(canvas):
    canvas.delete('all')
    SetPage(2)

    canvas.create_text(960, 50, text='Описание', font='JetBrainsMono 40')


def Animation(canvas):
    canvas.delete('all')
    SetPage(3)

    canvas.create_text(960, 50, text='Анимация', font='JetBrainsMono 40')


def Errors(canvas):
    canvas.delete('all')
    SetPage(4)

    canvas.create_text(960, 50, text='Погрешности', font='JetBrainsMono 40')


def Table(canvas):
    canvas.delete('all')
    SetPage(5)

    canvas.create_text(960, 50, text='Таблица', font='JetBrainsMono 40')


def Graph(canvas):
    canvas.delete('all')
    SetPage(6)

    canvas.create_text(960, 50, text='График', font='JetBrainsMono 40')


def Help(canvas):
    canvas.delete('all')
    SetPage(7)

    canvas.create_text(960, 50, text='Помощь', font='JetBrainsMono 40')


def Exit(canvas):
    canvas.delete('all')
    SetPage(8)


def Saves(canvas):
    canvas.delete('all')
    SetPage(9)

    canvas.create_text(960, 50, text='Сохранения', font='JetBrainsMono 40')
