from Apps.contrib.classes import Button
from Apps.contrib.fileworker import *
from tkinter.font import Font
from PIL import Image, ImageTk


# Заставка
def StartWindow(canvas):
    canvas.delete('all')
    SetPage(0)

    canvas.create_text(960, 540, text='Лабораторная работа', font='JetBrainsMono 50')


# Меню
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


# Описание
def Description(canvas):
    canvas.delete('all')
    SetPage(2)

    canvas.create_text(960, 50, text='Описание', font='JetBrainsMono 40')


# Анимация
def Animation(canvas):
    canvas.delete('all')
    SetPage(3)

    canvas.create_text(960, 50, text='Анимация', font='JetBrainsMono 40')


# Погрешности
def Errors(canvas):
    canvas.delete('all')
    SetPage(4)

    canvas.create_text(960, 50, text='Погрешности', font='JetBrainsMono 40')


# Таблица
def Table(canvas):
    canvas.delete('all')
    SetPage(5)

    canvas.create_text(960, 50, text='Таблица', font='JetBrainsMono 40')

    # Отрисовка таблицы
    Button(canvas, 960, 600, 1500, 700)
    for y in range(600-150, 601+250, 200):
        Button(canvas, 960, y, 1500, 100, anchor='n')
    Button(canvas, 960+350, 600, 1000, 700, anchor='e')
    for x in range(960-650, 960+750, 100):
        Button(canvas, x, 600-250, 100, 600, anchor='nw')
    # Цифры градусов таблицы
    y = 500
    for i in range(15, 76, 15):
        Button(canvas, 260, y, 100, 100, text=i, font='JetBrainsMono 25')
        y += 100
    # Цифры S таблицы
    for i in range(960-600, 960+301, 100):
        Button(canvas, i, 400, 100, 100, text='S', font='JetBrainsMono 25')
    # Надписи над таблицей
    Button(canvas, 960-150, 300, 1000, 100, text='Дальность полета (см)', font='JetBrainsMono 25')
    Button(canvas, 960+550, 300, 400, 100, text='(Все значения заносятся в см)', font='JetBrainsMono 25')


# График
def Graph(canvas):
    canvas.delete('all')
    SetPage(6)

    canvas.create_text(960, 50, text='График', font='JetBrainsMono 40')


# Помощь
def Help(canvas):
    canvas.delete('all')
    SetPage(7)

    canvas.create_text(960, 50, text='Помощь', font='JetBrainsMono 40')


# Подтверждение закрытия
def Exit(canvas):
    canvas.delete('all')
    SetPage(8)

    Button(canvas, 960, 540, 600, 400)
    canvas.create_text(960, 440, text='Вы уверены?', font='JetBrainsMono 30')
    Button(canvas, 810, 640, 200, 75, text='Да', font='JetBrainsMono 20')
    Button(canvas, 1110, 640, 200, 75, text='Нет', font='JetBrainsMono 20')


# Сохранения
def Saves(canvas):
    canvas.delete('all')
    SetPage(9)
    SetMemoryField('newsavename', '')

    canvas.create_text(960, 50, text='Сохранения', font='JetBrainsMono 40')
    Button(canvas, 960, 150, 1200, 80, text='Создать новое', font='JetBrainsMono 30')

    x = 275
    for file in GetSaves():
        Button(canvas, 710, x, 350, 80, text='перезаписать', font='JetBrainsMono 30', anchor='e')
        Button(canvas, 960, x, 500, 80, text=file[:-5], font='JetBrainsMono 30')
        Button(canvas, 1210, x, 350, 80, text='удалить', font='JetBrainsMono 30', anchor='w')
        x += 100


# Создать новое сохранение
def CreateSave(canvas):
    canvas.delete('all')
    SetPage(10)

    canvas.create_text(960, 50, text='Создать сохранение', font='JetBrainsMono 40')

    canvas.create_text(960, 300, text='Название:', font='JetBrainsMono 40')
    Button(canvas, 960, 400, 500, 80, text=GetMemoryField('newsavename'), font='JetBrainsMono 30')
    Button(canvas, 960, 625, 300, 80, text='Сохранить', font='JetBrainsMono 30')
