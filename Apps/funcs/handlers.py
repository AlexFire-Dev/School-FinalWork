from Apps.contrib.classes import ButtonClick
from Apps.funcs.inputs import *
from Apps.funcs.static import *


# Обработчик нажатий мыши
def Mouse(context):
    print(context['event'].x, context['event'].y)

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
    if ButtonClick(context['event'], 960, 150, 1200, 80, page=9).check():
        CreateSave(context['canvas'])
    SaveButtons = GetSaves()
    x = 275
    for SaveButton in SaveButtons:
        if ButtonClick(context['event'], 960, x, 500, 80, page=9).check():
            LoadSave(SaveButton)
            Menu(context['canvas'])
        if ButtonClick(context['event'], 1210, x, 350, 80, anchor='w', page=9).check():
            DeleteSave(SaveButton)
            Saves(context['canvas'])
        if ButtonClick(context['event'], 710, x, 350, 80, anchor='e', page=9).check():
            CreateNewSave(SaveButton[:-4])
            Menu(context['canvas'])
        x += 100

    # Создать новое сохранение
    if ButtonClick(context['event'], 960, 625, 300, 80, page=10).check():
        CheckSave(context['canvas'])

    # Подтверждение закрытия
    if ButtonClick(context['event'], 810, 640, 200, 75, page=8).check():
        context['root'].destroy()
    if ButtonClick(context['event'], 1110, 640, 200, 75, page=8).check():
        Menu(context['canvas'])


# Обработчик нажатий на клавиши
def Keyboard(context):

    # Выход в меню
    if context['event'].keysym == 'Escape':
        Menu(context['canvas'])

    # Создать название сохранения
    if not (context['event'].char in './') and GetPage() == 10:
        if context['event'].keysym != 'Return':
            NewSaveInput(context['event'])
            CreateSave(context['canvas'])
    if context['event'].keysym == 'BackSpace' and GetPage() == 10:
        NewSaveInputDelete()
        CreateSave(context['canvas'])
    if context['event'].keysym == 'Return' and GetPage() == 10:
        CheckSave(context['canvas'])


# Обработчик колеса мыши
def Wheel(context):

    # Прокрутка сохранений
    if GetPage() == 9:
        if context['event'].delta == -120:
            pass
        if context['event'].delta == 120:
            pass
