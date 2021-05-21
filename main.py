from tkinter import *

from Apps.funcs.handlers import *
from Apps.funcs.static import StartWindow, Exit
from Apps.contrib.contrib import *

FullScreen = True


def on_close():
    Exit(canvas)


def resize(event):
    global FullScreen

    if FullScreen:
        root.wm_attributes("-fullscreen", 0)
        root.wm_attributes("-topmost", 0)
        root.geometry('1920x1080')
        FullScreen = False
    else:
        root.wm_attributes("-fullscreen", 1)
        root.wm_attributes("-topmost", 1)
        FullScreen = True


root = Tk()
root.iconbitmap('Assets/Ico/main.ico')
root.title('Лабораторная работа!')
root.wm_attributes("-fullscreen", 1)
root.wm_attributes("-topmost", 1)
root.protocol('WM_DELETE_WINDOW', on_close)

canvas = Canvas(root, width=1920, height=1080, bg='white')
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
    Mouse(context)


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
root.bind('<F11>', resize)

root.mainloop()
