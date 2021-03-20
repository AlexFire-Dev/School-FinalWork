if __name__ == '__main__':

    # Глобальные переменные всего проекта

    # Страница программы
    page = 0

    # Память проекта
    mem = {
        'table': [],
        'error': [],
    }


# Работа со страницей
def SetPage(num):
    global page
    page = num


def GetPage():
    return page


# Работа с памятью
def GetMemory():
    return mem


def SetMemory(memory):
    global mem
    mem = memory


def GetMemoryField(field):
    return mem[f'{field}']


def SetMemoryField(field, value):
    global mem
    mem[f'{field}'] = value
