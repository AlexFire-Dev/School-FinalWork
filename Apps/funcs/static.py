from Apps.contrib.classes import Button, Tablica, ErrorsTable, HTable
from Apps.contrib.fileworker import *
from tkinter.font import Font
from tkinter import Canvas


# Заставка
def StartWindow(canvas: Canvas):
    canvas.delete('all')
    SetPage(0)

    canvas.create_text(960, 540, text='Лабораторная работа', font='JetBrainsMono 50')

    # Подсказка про выход в меню
    canvas.create_text(960, 1055, text='Для выхода в меню нажмите Esc', font='JetBrainsMono 15')


# Меню
def Menu(canvas: Canvas):
    canvas.delete('all')
    SetPage(1)

    canvas.create_text(960, 125, text='Меню', font='JetBrainsMono 70')

    buttons = ['Описание', 'Анимация', 'Погрешности', 'Таблицы', 'График', 'Вывод', 'Помощь', 'Завершить']
    x = 275
    for button in buttons:
        Button(canvas, 960, x, 400, 80, text=button, font='JetBrainsMono 30', color='#E5E5E5')
        x += 100

    Button(canvas, 1900, 20, 150, 50, text='Сохранения', font='JetBrainsMono 15', anchor='ne', color='#E5E5E5')

    # Подсказка
    canvas.create_text(960, 1055, text='Для выбора меню нажмите на него ЛКМ', font='JetBrainsMono 15')


# Описание
def Description(canvas: Canvas):
    canvas.delete('all')
    SetPage(2)

    canvas.create_text(960, 50, text='Исследование зависимости дальности полет от угла бросания.', font='JetBrainsMono 40')

    canvas.create_text(136, 138, text='Оборудование: баллистический пистолет, штатив, измерительная лента, лист белой и копировальной бумаги,\n'
                                      'ловушка для шарика',
                       font='JetBrainsMono 25', anchor='nw')
    canvas.create_text(136, 250, text='1. Укрепите баллистический пистолет в штативе таким образом, чтобы снаряд выбрасывался горизонтально\n'
                                      'и падал на стол. Измерьте высоту выстрела h, положите на место падения шарика лист белой бумаги, а сверху копировальной\n'
                                      '2. Произверите 10 выстрелов, измерьте расстояния до точек падения и занесите результаты в таблицу 1\n'
                                      '3. Установите баллистический пистолет на краю стола и произведите 10 выстрелов под углом 15⁰ к горизонту\n'
                                      'По анологии с п.2 измерьте расстояния и занесите в таблицу 2\n'
                                      '4. Проведите еще 4 серии выстрелов под углами 30⁰, 45⁰, 60⁰, 75⁰. Результаты занесите в таблицу 2\n'
                                      '5. Рассчитайте теоретическую дальность полета при углах бросания 15⁰, 30⁰, 45⁰, 60⁰, 75⁰. Результаты занесите в таблицу 2\n'
                                      '6. Проанализируйте полученный результат. Можно ли считать, что результаты эксеримента подтверждают теорию движения\n'
                                      'тела, брошенного под углом к горизонту.',
                       font='JetBrainsMono 20', anchor='nw')

    # Подсказка про выход в меню
    canvas.create_text(960, 1055, text='Для выхода в меню нажмите Esc', font='JetBrainsMono 15')


# Вывод
def Vivod(canvas: Canvas):
    canvas.delete('all')
    SetPage(13)

    canvas.create_text(960, 50, text='Вывод', font='JetBrainsMono 40')

    def CheckTable():
        memory = GetMemoryField('table')
        for y in range(0, 5):
            for x in range(0, 14):
                if memory[y][x] == '':
                    return False
        return True

    def parabola():
        Memory = GetMemoryField('table')
        for i in Memory:
            if not (float(i[13]) - float(i[11]) >= float(i[10])) and (float(i[13]) + float(i[11]) <= float(i[10])):
                return False
        return True

    if CheckTable():
        if parabola():
            canvas.create_text(960, 540, text='Результаты подтверждают теорию тела брошенного под углом к горизонту', font='JetBrainsMono 35')
        else:
            canvas.create_text(960, 540, text='Результаты не подтверждают теорию тела брошенного под углом к горизонту', font='JetBrainsMono 35')
    else:
        canvas.create_text(960, 540, text='Заполните все поля таблиц!', font='JetBrainsMono 60')

    # Подсказка про выход в меню
    canvas.create_text(960, 1055, text='Для выхода в меню нажмите Esc', font='JetBrainsMono 15')


# Анимация
def Animation(canvas: Canvas):
    global target

    canvas.delete('all')
    SetPage(3)
    try:
        canvas.delete(target)
    except:
        pass

    canvas.create_text(960, 50, text='Анимация', font='JetBrainsMono 40')

    canvas.create_rectangle(365, 770, 1925, 910)
    canvas.create_rectangle(365, 780, 315, 797)
    Button(canvas, 1780, 845, 100, 50, text='Старт', font='JetBrainsMono 15')
    canvas.create_polygon(316, 753, 343, 767, 310, 812, 284, 798, fill='black')

    # Подсказка про выход в меню
    canvas.create_text(960, 1055, text='Для выхода в меню нажмите Esc', font='JetBrainsMono 15')


# Движение в анимации
def Anim(canvas: Canvas):
    import time
    global target, progress

    try:
        if progress:
            return
    except:
        pass

    progress = True
    target = canvas.create_oval(0-5, 0-5, 0+5, 0+5, fill='black')
    canvas.delete('t')

    a = 0.0010233918128654976
    b = -2.149122807017545
    c = 1358.289473684211

    for x in range(150, 1920+1):
        y = a * x ** 2 + b * x + c
        if y <= 765 and CheckPage(3):
            canvas.coords(target, x - 5, y - 5, x + 5, y + 5)
            canvas.create_oval(x - 1, y - 1, x + 1, y + 1, tag='t')
            canvas.update()
            time.sleep(0.001)
        elif not CheckPage(3):
            break

    progress = False


# Погрешности
def Errors(canvas: Canvas, table: ErrorsTable):
    canvas.delete('all')
    SetPage(4)

    canvas.create_text(960, 50, text='Погрешности', font='JetBrainsMono 40')

    # Отрисовка таблицы со значениями
    Button(canvas, 960, 560, 700, 150, text='Погрешность угла, °', font='JetBrainsMono 35', anchor='se')
    Button(canvas, 960, 560, 700, 150, anchor='sw')
    Button(canvas, 960, 560, 700, 150, text='Погрешность длины, мм', font='JetBrainsMono 35', anchor='ne')
    Button(canvas, 960, 560, 700, 150, anchor='nw')

    x = 560 - 75
    for field in GetMemoryField('error'):
        canvas.create_text(980, x, text=field, font='JetBrainsMono 35', anchor='w')
        x += 150
    table.createcursor(canvas)

    # Подсказка про выход в меню
    canvas.create_text(960, 1055, text='Для выхода в меню нажмите Esc', font='JetBrainsMono 15')


def Table_1(canvas: Canvas, tablica: Tablica):
    canvas.delete('all')
    SetPage(11)
    TableMemory = GetMemoryField('table-1')

    tablica.handler()

    canvas.create_text(960, 50, text='Таблица', font='JetBrainsMono 40')
    # Кнопки переключения таблиц
    Button(canvas, 960, 130, 60, 50, text='1', font='JetBrainsMono 25', anchor='e', color='#E5E5E5')
    Button(canvas, 960, 130, 60, 50, text='2', font='JetBrainsMono 25', anchor='w', color='#E5E5E5')

    # Отрисовка таблицы
    Button(canvas, 210, 300, 1600, 300, anchor='nw')
    # Надписи над таблицей
    Button(canvas, 960 + 250, 350, 1000, 100, text='Дальность полета (см)', font='JetBrainsMono 25', anchor='e')
    Button(canvas, 960 + 850, 350, 600, 100, text='(Расстояния в см, скорости в см/с)', font='JetBrainsMono 25',
           anchor='e')
    for s in range(1, 11):
        Button(canvas, 960 - (850 - s * 100), 400, 100, 100, text='S', font='JetBrainsMono 25', anchor='nw')
        canvas.create_text(960 - (785 - s * 100), 465, text=s, font='JetBrainsMono 12')
    Button(canvas, 960 + 850, 400, 150, 100, text='Δϑ  ', font='JetBrainsMono 25', anchor='ne')
    canvas.create_text(1750, 462, text='0', font='JetBrainsMono 12')
    Button(canvas, 960 + 700, 400, 150, 100, text='ϑ     ', font='JetBrainsMono 25', anchor='ne')
    canvas.create_text(1593, 462, text='0 эксп', font='JetBrainsMono 12')
    Button(canvas, 960 + 550, 400, 150, 100, text='ΔS  ', font='JetBrainsMono 25', anchor='ne')
    canvas.create_text(1454, 462, text='ср', font='JetBrainsMono 12')
    Button(canvas, 960 + 400, 400, 150, 100, text='S  ', font='JetBrainsMono 25', anchor='ne')
    canvas.create_text(1293, 462, text='ср', font='JetBrainsMono 12')
    for x in range(960 - 650, 960 + 251, 100):
        canvas.create_line(x, 500, x, 600)
    for x in range(960 + 400, 960 + 850, 150):
        canvas.create_line(x, 500, x, 600)

    Button(canvas, 960 - 150, 800, 300, 100, text='h', font='JetBrainsMono 25', anchor='ne')
    Button(canvas, 960, 800, 300, 100, anchor='n')
    Button(canvas, 960 + 150, 800, 300, 100, text='Изменить', font='JetBrainsMono 25', anchor='nw')

    # Отрисовка значенй таблицы
    for y in range(tablica.height):
        for x in range(tablica.width):
            canvas.create_text(960 - 745 + 100 * x, 550 + 100 * y, text=TableMemory[y][x], font='JetBrainsMono 25',
                               anchor='w')
    for y in range(tablica.height):
        for x in range(4):
            canvas.create_text(960 + 255 + 150 * x, 550 + 100 * y, text=TableMemory[y][x + 10], font='JetBrainsMono 25',
                               anchor='w')

    # Курсор
    tablica.createcursor(canvas)

    canvas.create_text(820, 850, text=GetMemoryField('h'), font='JetBrainsMono 25', anchor='w')

    # Подсказка про выход в меню
    canvas.create_text(960, 1055, text='Для выхода в меню нажмите Esc', font='JetBrainsMono 15')


# Изменить h
def ChangeH(canvas: Canvas, tablica: Tablica, htable: HTable):
    canvas.delete('all')
    SetPage(12)
    TableMemory = GetMemoryField('table-1')

    canvas.create_text(960, 50, text='Таблица', font='JetBrainsMono 40')

    # Отрисовка таблицы
    Button(canvas, 210, 300, 1600, 300, anchor='nw')
    # Надписи над таблицей
    Button(canvas, 960 + 250, 350, 1000, 100, text='Дальность полета (см)', font='JetBrainsMono 25', anchor='e')
    Button(canvas, 960 + 850, 350, 600, 100, text='(Расстояния в см, скорости в см/с)', font='JetBrainsMono 25',
           anchor='e')
    for s in range(1, 11):
        Button(canvas, 960 - (850 - s * 100), 400, 100, 100, text='S', font='JetBrainsMono 25', anchor='nw')
        canvas.create_text(960 - (785 - s * 100), 465, text=s, font='JetBrainsMono 12')
    Button(canvas, 960 + 850, 400, 150, 100, text='Δϑ  ', font='JetBrainsMono 25', anchor='ne')
    canvas.create_text(1750, 462, text='0', font='JetBrainsMono 12')
    Button(canvas, 960 + 700, 400, 150, 100, text='ϑ     ', font='JetBrainsMono 25', anchor='ne')
    canvas.create_text(1593, 462, text='0 эксп', font='JetBrainsMono 12')
    Button(canvas, 960 + 550, 400, 150, 100, text='ΔS  ', font='JetBrainsMono 25', anchor='ne')
    canvas.create_text(1454, 462, text='ср', font='JetBrainsMono 12')
    Button(canvas, 960 + 400, 400, 150, 100, text='S  ', font='JetBrainsMono 25', anchor='ne')
    canvas.create_text(1293, 462, text='ср', font='JetBrainsMono 12')
    for x in range(960 - 650, 960 + 251, 100):
        canvas.create_line(x, 500, x, 600)
    for x in range(960 + 400, 960 + 850, 150):
        canvas.create_line(x, 500, x, 600)

    Button(canvas, 960 - 150, 800, 300, 100, text='h', font='JetBrainsMono 25', anchor='ne')
    Button(canvas, 960, 800, 300, 100, anchor='n')
    Button(canvas, 960 + 150, 800, 300, 100, text='Сохранить', font='JetBrainsMono 25', anchor='nw')

    # Отрисовка значенй таблицы
    for y in range(tablica.height):
        for x in range(tablica.width):
            canvas.create_text(960 - 745 + 100 * x, 550 + 100 * y, text=TableMemory[y][x], font='JetBrainsMono 25',
                               anchor='w')
    for y in range(tablica.height):
        for x in range(4):
            canvas.create_text(960 + 255 + 150 * x, 550 + 100 * y, text=TableMemory[y][x + 10], font='JetBrainsMono 25',
                               anchor='w')

    # Курсор
    htable.createcursor(canvas)

    canvas.create_text(820, 850, text=GetMemoryField('h'), font='JetBrainsMono 25', anchor='w')

    # Подсказка про выход в меню
    canvas.create_text(960, 1055, text='Для выхода в меню нажмите Esc', font='JetBrainsMono 15')


# Таблица
def Table(canvas: Canvas, tablica: Tablica):
    canvas.delete('all')
    SetPage(5)
    TableMemory = GetMemoryField('table')

    canvas.create_text(960, 50, text='Таблица', font='JetBrainsMono 40')
    # Кнопки переключения таблиц
    Button(canvas, 960, 130, 60, 50, text='1', font='JetBrainsMono 25', anchor='e', color='#E5E5E5')
    Button(canvas, 960, 130, 60, 50, text='2', font='JetBrainsMono 25', anchor='w', color='#E5E5E5')

    # Отрисовка таблицы
    Button(canvas, 960, 650, 1700, 700)
    # Надписи над таблицей
    Button(canvas, 960 + 250, 350, 1000, 100, text='Дальность полета (см)', font='JetBrainsMono 25', anchor='e')
    Button(canvas, 960 + 850, 350, 600, 100, text='(Все значения заносятся в см)', font='JetBrainsMono 25', anchor='e')
    for s in range(1, 11):
        Button(canvas, 960 - (850 - s * 100), 400, 100, 100, text='S', font='JetBrainsMono 25', anchor='nw')
        canvas.create_text(960 - (785 - s * 100), 465, text=s, font='JetBrainsMono 12')
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
        canvas.create_line(960 - 750, y, 960 + 850, y)
    for x in range(960 - 650, 960 + 251, 100):
        canvas.create_line(x, 500, x, 1000)
    for x in range(960 + 400, 960 + 850, 150):
        canvas.create_line(x, 500, x, 1000)
    # Надписи сбоку таблицы
    Button(canvas, 960 - 850, 300, 100, 200, text='α', font='JetBrainsMono 25', anchor='nw')
    y = 500
    for a in range(15, 76, 15):
        Button(canvas, 960 - 850, y, 100, 100, text=f'{a}⁰', font='JetBrainsMono 25', anchor='nw')
        y += 100

    # Отрисовка значенй таблицы
    for y in range(tablica.height):
        for x in range(tablica.width):
            canvas.create_text(960 - 745 + 100 * x, 550 + 100 * y, text=TableMemory[y][x], font='JetBrainsMono 25',
                               anchor='w')
    for y in range(tablica.height):
        for x in range(4):
            canvas.create_text(960 + 255 + 150 * x, 550 + 100 * y, text=TableMemory[y][x + 10], font='JetBrainsMono 25',
                               anchor='w')

    # Курсор
    tablica.createcursor(canvas)

    # Подсказка про выход в меню
    canvas.create_text(960, 1055, text='Для выхода в меню нажмите Esc', font='JetBrainsMono 15')


# График
def Graph(canvas: Canvas):
    def CheckTable():
        memory = GetMemoryField('table')
        for y in range(0, 5):
            for x in range(0, 14):
                if memory[y][x] == '':
                    return False
        return True

    canvas.delete('all')
    SetPage(6)

    canvas.create_text(960, 50, text='График', font='JetBrainsMono 40')

    # Подсказка про выход в меню
    canvas.create_text(960, 1055, text='Для выхода в меню нажмите Esc', font='JetBrainsMono 15')

    Memory = GetMemoryField('table')
    Errors = GetMemoryField('error')

    canvas.create_line(150, 980, 150, 150, width=3, arrow='last')
    canvas.create_line(149, 980, 1920 - 150, 980, width=3, arrow='last')
    canvas.create_text(150, 120, text='S, см', font='JetBrainsMono 20')
    canvas.create_text(1835, 980, text='α, ⁰', font='JetBrainsMono 20')

    x = 150
    for a in range(0, 90, 15):
        canvas.create_oval(x - 3, 980 - 3, x + 3, 980 + 3, fill='black')
        canvas.create_text(x, 995, text=f'{a}', font='JetBrainsMono 15')
        x += 300

    if CheckTable():
        def parabola():
            for i in Memory:
                if not (float(i[13]) - float(i[11]) > float(i[10])) and (float(i[13]) + float(i[11]) < float(i[10])):
                    return False
            return True

        x = 450
        for a in range(5):
            y = (750 / float(Memory[2][13])) * float(Memory[a][13])
            canvas.create_oval(x - 3, 980 - y - 3, x + 3, 980 - y + 3, fill='black')
            canvas.create_text(120, 980 - y, text=f'{Memory[a][13]}', font='JetBrainsMono 15')
            canvas.create_oval(150 - 3, 980 - y - 3, 150 + 3, 980 - y + 3, fill='black')
            x += 300
        y = (750 / float(Memory[2][13])) * float(Memory[1][13])
        x1, y1 = 750, 980 - y
        x2, y2 = 1050, 980 - 750
        x3, y3 = 1350, 980 - y

        a = (y3 - (x3 * (y2 - y1) + x2 * y1 - x1 * y2) / (x2 - x1)) / (x3 * (x3 - x1 - x2) + x1 * x2)
        b = (y2 - y1) / (x2 - x1) - a * (x1 + x2)
        c = (x2 * y1 - x1 * y2) / (x2 - x1) + a * x1 * x2

        for x in range(150, 1920 - 150 + 1):
            y = a * x ** 2 + b * x + c
            if y <= 980:
                canvas.create_oval(x - 1, y - 1, x + 1, y + 1)

        if not parabola():
            canvas.create_text(960, 700, text='Значения не попадают на 1 кривую!', font='JetBrainsMono 40')
    else:
        canvas.create_text(960, 540, text='Заполните все поля таблиц!', font='JetBrainsMono 60')


# Помощь
def Help(canvas: Canvas):
    canvas.delete('all')
    SetPage(7)

    canvas.create_text(960, 50, text='Помощь', font='JetBrainsMono 40')

    # Подсказка про выход в меню
    canvas.create_text(960, 1055, text='Для выхода в меню нажмите Esc', font='JetBrainsMono 15')


# Подтверждение закрытия
def Exit(canvas: Canvas):
    canvas.delete('all')
    SetPage(8)

    Button(canvas, 960, 540, 600, 400)
    canvas.create_text(960, 440, text='Вы уверены?', font='JetBrainsMono 30')
    Button(canvas, 810, 640, 200, 75, text='Да', font='JetBrainsMono 20', color='#E5E5E5')
    Button(canvas, 1110, 640, 200, 75, text='Нет', font='JetBrainsMono 20', color='#E5E5E5')


# Сохранения
def Saves(canvas: Canvas):
    canvas.delete('all')
    SetPage(9)
    SetMemoryField('newsavename', '')

    canvas.create_text(960, 50, text='Сохранения', font='JetBrainsMono 40')
    Button(canvas, 960, 150, 1200, 80, text='Создать новое', font='JetBrainsMono 30', color='#E5E5E5')

    x = 275
    for file in GetSaves():
        Button(canvas, 710, x, 350, 80, text='перезаписать', font='JetBrainsMono 30', anchor='e', color='#E5E5E5')
        Button(canvas, 960, x, 500, 80, text=file[:-5], font='JetBrainsMono 30', color='#E5E5E5')
        Button(canvas, 1210, x, 350, 80, text='удалить', font='JetBrainsMono 30', anchor='w', color='#E5E5E5')
        x += 100

    # Подсказка про выход в меню
    canvas.create_text(960, 1055, text='Для выхода в меню нажмите Esc', font='JetBrainsMono 15')


# Создать новое сохранение
def CreateSave(canvas: Canvas):
    canvas.delete('all')
    SetPage(10)

    canvas.create_text(960, 50, text='Создать сохранение', font='JetBrainsMono 40')

    canvas.create_text(960, 300, text='Название:', font='JetBrainsMono 40')
    Button(canvas, 960, 400, 500, 80, text=GetMemoryField('newsavename'), font='JetBrainsMono 30')
    Button(canvas, 960, 625, 300, 80, text='Сохранить', font='JetBrainsMono 30', color='#E5E5E5')

    # Подсказка про выход в меню
    canvas.create_text(960, 1055, text='Для выхода в меню нажмите Esc', font='JetBrainsMono 15')
