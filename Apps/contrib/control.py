if __name__ == '__main__':
    # Глобальные переменные всего проекта
    page = 0


def ChangePage(num):
    global page

    page = num


def GetPage():
    global page
    return page
