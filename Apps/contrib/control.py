from Apps.contrib.contrib import log

if __name__ == '__main__':

    # Глобальные переменные всего проекта

    # Страница программы
    page = 0

    # Память проекта
    mem = {}


# Работа со страницей
def SetPage(num: int):
    global page
    page = num


def GetPage():
    return page


def CheckPage(integer: int):
    if GetPage() == integer:
        return True
    else:
        return False


# Работа с памятью
def SetDefaultMemory():
    table = [''] * 5
    for i in range(0, len(table)):
        table[i] = [''] * 14
    table_1 = ['']
    table_1[0] = [''] * 14
    Memory = {
        'newsavename': '',
        'h': '',
        'error': ['3', '5'],
        'table': table,
        'table-1': table_1,
    }

    SetMemory(Memory)


def SetStockMemory():
    error = ['3', '5']
    table = [
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ]

    table_1 = [
        ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ]
    Memory = {
        'newsavename': '',
        'h': '0',
        'error': error,
        'table': table,
        'table-1': table_1,
    }

    SetMemory(Memory)
    log('MemorySet', way=['Memory'])


def GetMemory():
    return mem


def SetMemory(memory: dict):
    global mem
    mem = memory


def GetMemoryField(field):
    global mem
    MemoryField = mem.get(f'{field}')
    log(MemoryField, way=['GetMemoryField'])
    return MemoryField


def SetMemoryField(field, value):
    global mem
    mem[f'{field}'] = value
