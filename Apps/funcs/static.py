from Apps.contrib.control import ChangePage


def StartWindow(canvas):
    global page

    canvas.delete('all')
    ChangePage(0)

    canvas.create_text(960, 540, text='Лабораторная работа', font='JetBrainsMono 50')
