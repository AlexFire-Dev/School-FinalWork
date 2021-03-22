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
def Table(canvas, tablica):
    canvas.delete('all')
    SetPage(5)
    TableMemory = GetMemoryField('table')

    canvas.create_text(960, 50, text='Таблица', font='JetBrainsMono 40')

    # Отрисовка значенй таблицы
    for y in range(5):
        for x in range(5):
            canvas.create_text(960-740+100*x, 650-100+100*y, text=TableMemory[y][x], font='JetBrainsMono 25', anchor='w')

    # Курсор
    tablica.createcursor(canvas)

    # Отрисовка таблицы
    Button(canvas, 960, 650, 1700, 700)
    # Надписи над таблицей
    Button(canvas, 960+250, 350, 1000, 100, text='Дальность полета (см)', font='JetBrainsMono 25', anchor='e')
    Button(canvas, 960+850, 350, 600, 100, text='(Все значения заносятся в см)', font='JetBrainsMono 25', anchor='e')
    for s in range(1, 11):
        Button(canvas, 960 - (850-s*100), 400, 100, 100, text='S', font='JetBrainsMono 25', anchor='nw')
        canvas.create_text(960-(785-s*100), 465, text=s, font='JetBrainsMono 12')
    Button(canvas, 960 + 850, 400, 150, 100, text='S   ', font='JetBrainsMono 25', anchor='ne')
    canvas.create_text(1750, 462, text='теор', font='JetBrainsMono 12')
    Button(canvas, 960 + 700, 400, 150, 100, text='S  ±ΔS  ', font='JetBrainsMono 25', anchor='ne')
    canvas.create_text(1554, 462, text='ср', font='JetBrainsMono 12')
    canvas.create_text(1637, 462, text='ср', font='JetBrainsMono 12')
    Button(canvas, 960 + 550, 400, 150, 100, text='ΔS  ', font='JetBrainsMono 25', anchor='ne')
    canvas.create_text(1454, 462, text='ср', font='JetBrainsMono 12')
    Button(canvas, 960 + 400, 400, 150, 100, text='S  ', font='JetBrainsMono 25', anchor='ne')
    canvas.create_text(1293, 462, text='ср', font='JetBrainsMono 12')
    for y in range(600, 1001, 100):
        canvas.create_line(960-750, y, 960+850, y)
    for x in range(960-650, 960+251, 100):
        canvas.create_line(x, 500, x, 1000)
    for x in range(960+400, 960+850, 150):
        canvas.create_line(x, 500, x, 1000)
    # Надписи сбоку таблицы
    Button(canvas, 960-850, 300, 100, 200, text='α', font='JetBrainsMono 25', anchor='nw')
    y = 500
    for a in range(15, 76, 15):
        Button(canvas, 960 - 850, y, 100, 100, text=f'{a}⁰', font='JetBrainsMono 25', anchor='nw')
        y += 100


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
