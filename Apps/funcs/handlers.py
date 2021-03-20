from Apps.contrib.control import *
from Apps.contrib.classes import ButtonClick
from Apps.contrib.fileworker import *
from Apps.funcs.static import *


# Обработчик нажатий мыши
def Mouse(context):

    # Меню
    MenuButtons = [
        [Description, context['canvas']],
        [Animation, context['canvas']],
        [Errors, context['canvas']],
        [Table, context['canvas']],
        [Graph, context['canvas']],
        [Help, context['canvas']],
        [Exit, context['canvas']],
    ]
    x = 325
    for MenuButton in MenuButtons:
        if ButtonClick(context['event'], 960, x, 400, 80, page=1).check():
            MenuButton[0](MenuButton[1])
        x += 100
    if ButtonClick(context['event'], 1900, 20, 150, 50, page=1, anchor='ne').check():
        Saves(context['canvas'])

    # Сохранения
    SaveButtons = GetSaves()
    x = 275
    for SaveButton in SaveButtons:
        if ButtonClick(context['event'], 960, x, 500, 80, page=9).check():
            LoadSave(SaveButton)
        x += 100


# Обработчик нажатий на клавиши
def Keyboard(context):

    if context['event'].keysym == 'Escape':
        Menu(context['canvas'])


# Обработчик колеса мыши
def Wheel(context):

    if GetPage() == 9:
        if context['event'].delta == -120:
            pass
        if context['event'].delta == 120:
            pass
