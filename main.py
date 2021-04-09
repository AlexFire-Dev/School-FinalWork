from tkinter import *

from Apps.funcs.handlers import *
from Apps.funcs.static import StartWindow, Exit
from Apps.contrib.contrib import *


def on_close():
    Exit(canvas)


root = Tk()
root.iconbitmap('Assets/Ico/main.ico')
root.title('Лабораторная работа!')
root.geometry('1920x1080')
root.protocol('WM_DELETE_WINDOW', on_close)

canvas = Canvas(root, width=3840, height=2160, bg='white')
canvas.pack()

StartWindow(canvas)
SetDefaultMemory()
StartSession()


# Передаем параметры в обработчик мыши
def MouseHandler(event):
    context = {
        'event': event,
        'canvas': canvas,
        'root': root,
    }
    PerfCheck(func=Mouse, name='MouseButton', args=[context])


# Передаем параметры в обработчик клавиатуры
def KeyboardHandler(event):
    context = {
        'event': event,
        'canvas': canvas,
        'root': root,
    }
    Keyboard(context)


# Передаем параметры в обработчик колеса мыши
def MouseWheelHandler(event):
    context = {
        'event': event,
        'canvas': canvas,
        'root': root,
    }
    Wheel(context)


root.bind('<Button-1>', MouseHandler)
root.bind('<KeyRelease>', KeyboardHandler)
root.bind('<MouseWheel>', MouseWheelHandler)

root.mainloop()
