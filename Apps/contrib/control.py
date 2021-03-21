if __name__ == '__main__':

    # Глобальные переменные всего проекта

    # Страница программы
    page = 0

    # Память проекта
    mem = {
        'table': [],
        'error': [],
        'newsavename': '',
    }


# Работа со страницей
def SetPage(num):
    global page
    page = num


def GetPage():
    return page


# Работа с памятью
def SetDefaultMemory():
    table = [''] * 5
    for i in range(0, len(table)):
        table[i] = [''] * 14
    Memory = {
        'table': table,
        'error': [],
        'newsavename': '',
    }

    SetMemory(Memory)


def GetMemory():
    return mem


def SetMemory(memory):
    global mem
    mem = memory


def GetMemoryField(field):
    global mem
    MemoryField = mem[f'{field}']
    return MemoryField


def SetMemoryField(field, value):
    global mem
    mem[f'{field}'] = value
