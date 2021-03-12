from tkinter import *

from Apps.classes.button import Button


root = Tk()
root.iconbitmap('Assets/Ico/main.ico')
root.title('Лабораторная работа!')
root.geometry('1920x1080')

canvas = Canvas(root, width=3840, height=2160, bg='white')
canvas.pack()


# Обработчик нажатий мыши
def MouseHandler(event):
    print(event.x, event.y)

    Button(canvas, pos_x=event.x, pos_y=event.y, width=100, height=100, anchor='nw')


# Обработчик нажатий на клавиши
def KeyboardHandler(event):
    pass


root.bind('<Button-1>', MouseHandler)
root.bind('<KeyRelease>', KeyboardHandler)

root.mainloop()
