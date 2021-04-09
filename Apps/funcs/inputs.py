from Apps.contrib.control import *
from Apps.contrib.fileworker import CreateNewSave
from Apps.funcs.static import Menu
from tkinter import Canvas, Event


# Добавляет символ к названию сохранения
def NewSaveInput(event):
    if len(GetMemoryField('newsavename')) < 15:
        NewValue = GetMemoryField('newsavename') + event.char
        SetMemoryField('newsavename', value=NewValue)


# Удаляет последний символ в названии сохранения
def NewSaveInputDelete():
    NewValue = GetMemoryField('newsavename')[:-1]
    SetMemoryField('newsavename', value=NewValue)


# Проверяет ошибки при создании сохранения
def CheckSave(canvas: Canvas):
    if CreateNewSave(GetMemoryField('newsavename')) == 0:
        Menu(canvas)
    elif CreateNewSave(GetMemoryField('newsavename')) == 1:
        canvas.create_rectangle(960 - 250, 465 - 20, 960 + 250, 465 + 20, outline='white', fill='white')
        canvas.create_text(960, 465, text='Такой файл уже существует!', font='JetBrainsMono 15', fill='red')
    elif CreateNewSave(GetMemoryField('newsavename')) == 2:
        canvas.create_rectangle(960 - 250, 465 - 20, 960 + 250, 465 + 20, outline='white', fill='white')
        canvas.create_text(960, 465, text='Название не может быть пустым!', font='JetBrainsMono 15', fill='red')
    elif CreateNewSave(GetMemoryField('newsavename')) == 3:
        canvas.create_rectangle(960 - 250, 465 - 20, 960 + 250, 465 + 20, outline='white', fill='white')
        canvas.create_text(960, 465, text='Все слоты памяти заняты!', font='JetBrainsMono 15', fill='red')
