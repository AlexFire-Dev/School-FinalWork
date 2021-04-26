from Apps.contrib.classes import ButtonClick, Tablica, ErrorsTable, HTable
from Apps.contrib.control import SetStockMemory
from Apps.contrib.contrib import log
from Apps.funcs.inputs import *
from Apps.funcs.static import *
import time


# Обработчик нажатий мыши
def Mouse(context: dict):
    global tablica, errorstable, htable
    log(context['event'].x, context['event'].y, way=['coords'])

    # Меню
    if CheckPage(1):
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
            if ButtonClick(context['event'], 960, x, 400, 80).check():
                if MenuButton[0] == Table:
                    tablica = Tablica(width=10, height=5, canvas=context.get('canvas'))
                    Table(MenuButton[1], tablica)
                    return
                elif MenuButton[0] == Errors:
                    errorstable = ErrorsTable()
                    Errors(MenuButton[1], errorstable)
                    return
                else:
                    MenuButton[0](MenuButton[1])
                    return
            x += 100
        if ButtonClick(context['event'], 1900, 20, 150, 50, anchor='ne').check():
            Saves(context['canvas'])
            return

    # Сохранения
    if CheckPage(9):
        if ButtonClick(context['event'], 960, 150, 1200, 80).check():
            CreateSave(context['canvas'])
            return
        SaveButtons = GetSaves()
        x = 275
        for SaveButton in SaveButtons:
            if ButtonClick(context['event'], 960, x, 500, 80).check():
                LoadSave(SaveButton)
                Menu(context['canvas'])
                return
            if ButtonClick(context['event'], 1210, x, 350, 80, anchor='w').check():
                DeleteSave(SaveButton)
                Saves(context['canvas'])
                return
            if ButtonClick(context['event'], 710, x, 350, 80, anchor='e').check():
                ReCreate(SaveButton)
                Menu(context['canvas'])
                return
            x += 100

    # Создать новое сохранение
    if CheckPage(10):
        if ButtonClick(context['event'], 960, 625, 300, 80).check():
            CheckSave(context['canvas'])
            return

    # Подтверждение закрытия
    if CheckPage(8):
        if ButtonClick(context['event'], 810, 640, 200, 75).check():
            context['root'].destroy()
            return
        if ButtonClick(context['event'], 1110, 640, 200, 75).check():
            Menu(context['canvas'])
            return

    # Кнопки таблиц
    if CheckPage(5) or CheckPage(11):
        if ButtonClick(context['event'], 960, 130, 60, 50, anchor='e').check():
            tablica = Tablica(width=10, height=1, memory='table-1', canvas=context.get('canvas'))
            Table_1(canvas=context['canvas'], tablica=tablica)
            return
        elif ButtonClick(context['event'], 960, 130, 60, 50, anchor='w').check():
            tablica = Tablica(width=10, height=5, canvas=context.get('canvas'))
            Table(canvas=context['canvas'], tablica=tablica)
            return

    # Таблица 1
    if CheckPage(11):
        if ButtonClick(context.get('event'), 960+150, 800, 300, 100, anchor='nw').check():
            tablica = Tablica(width=10, height=1, memory='table-1', canvas=context.get('canvas'))
            htable = HTable()
            ChangeH(context.get('canvas'), tablica=tablica, htable=htable)
            return

    # Изменить h
    if CheckPage(12):
        if ButtonClick(context.get('event'), 960+150, 800, 300, 100, anchor='nw').check():
            log('Ok!', way=['ClickPass_12'])
            tablica = Tablica(width=10, height=1, memory='table-1', canvas=context.get('canvas'))
            Table_1(context.get('canvas'), tablica=tablica)
            return


# Обработчик нажатий на клавиши
def Keyboard(context: dict):
    global tablica, errorstable, htable

    # Выход в меню
    if context['event'].keysym == 'Escape':
        Menu(context['canvas'])
        return

    # Задание стандартной памяти
    if context.get('event').keysym == 'F3':
        SetStockMemory()
        log('Done!', way=['Memory'])

        if GetPage() == 5:
            Table(context.get('canvas'), tablica)
            return
        elif GetPage() == 11:
            Table_1(context.get('canvas'), tablica)
            return
        elif GetPage() == 4:
            Errors(context.get('canvas'), errorstable)
            return
        elif GetPage() == 12:
            ChangeH(context.get('canvas'), tablica, htable)
            return

    # Создать название сохранения
    if CheckPage(10):
        if not (context.get('event').char in './'):
            if context['event'].keysym != 'Return':
                NewSaveInput(context['event'])
                CreateSave(context['canvas'])
                return
        if context['event'].keysym == 'BackSpace':
            NewSaveInputDelete()
            CreateSave(context.get('canvas'))
            return
        if context['event'].keysym == 'Return':
            CheckSave(context['canvas'])
            return

    # Заполнение таблицы
    if CheckPage(5) or CheckPage(11):
        if context['event'].keysym == 'Right' or context['event'].keysym == 'Left' or context['event'].keysym == 'Up' or context['event'].keysym == 'Down' or context['event'].keysym == 'BackSpace':
            tablica.keyboard(context['event'].keysym, context['canvas'])
            tablica.createcursor(context['canvas'])
            return
        if ((context['event'].keysym in '0123456789') or context['event'].char == '.' and not ('.' in GetMemoryField(tablica.memory)[tablica.y][tablica.x])) and len(GetMemoryField(tablica.memory)[tablica.y][tablica.x]) < 2:
            tablica.addsym(context['event'].char, context['canvas'])
            tablica.createcursor(context['canvas'])
            return

    # Заполнение погрешности
    if CheckPage(4):
        if context['event'].keysym == 'Up' or context['event'].keysym == 'Down' or context['event'].keysym == 'BackSpace':
            errorstable.keyboard(context['event'].keysym, context['canvas'])
            errorstable.createcursor(context['canvas'])
            return
        if (context['event'].keysym in '0123456789') and len(GetMemoryField(errorstable.memory)[errorstable.y]) < 2:
            errorstable.addsym(context['event'].char, context['canvas'])
            errorstable.createcursor(context['canvas'])
            return

    # Изменение h
    if CheckPage(12):
        if (context['event'].keysym in '0123456789') and len(GetMemoryField(htable.memory)) < 2:
            htable.addsym(context['event'].char, context['canvas'])
            htable.createcursor(context['canvas'])
            return
        if context['event'].keysym == 'BackSpace':
            htable.keyboard(context['event'].keysym, context['canvas'])
            htable.createcursor(context['canvas'])
            return


# Обработчик колеса мыши
def Wheel(context: dict):

    # Прокрутка сохранений
    if CheckPage(9):
        if context['event'].delta == -120:
            pass
        if context['event'].delta == 120:
            pass
