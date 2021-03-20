from tkinter import *

from Apps.funcs.handlers import *
from Apps.funcs.static import StartWindow


root = Tk()
root.iconbitmap('Assets/Ico/main.ico')
root.title('Лабораторная работа!')
root.geometry('1920x1080')

canvas = Canvas(root, width=3840, height=2160, bg='white')
canvas.pack()

StartWindow(canvas)


# Передаем параметры в обработчик мыши
def MouseHandler(event):
    context = {
        'event': event,
        'canvas': canvas,
        'root': root,
    }
    Mouse(context)


# Передаем параметры в обработчик клавиатуры
def KeyboardHandler(event):
    context = {
        'event': event,
        'canvas': canvas,
        'root': root,
    }
    Keyboard(context)


root.bind('<Button-1>', MouseHandler)
root.bind('<KeyRelease>', KeyboardHandler)

root.mainloop()
