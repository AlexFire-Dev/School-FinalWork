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
        'error': ['2', '5'],
        'table': table,
        'table-1': table_1,
    }

    SetMemory(Memory)


def SetStockMemory():
    error = ['2', '5']
    table = [
        ['5', '7', '6', '5', '6', '4', '5', '7', '6', '5', 5.6, '0.9', '5.6±0.9', '5.5'],
        ['9', '10', '11', '10', '8', '9', '10', '9', '11', '10', 9.7, '0.9', '9.7±0.9', '9.6'],
        ['11', '13', '10', '9', '12', '13', '12', '11', '12', '11', 11.4, '1.1', '11.4±1.1', '11.0'],
        ['10', '9', '10', '11', '10', '8', '9', '11', '9', '10', 9.7, '0.9', '9.7±0.9', '9.6'],
        ['5', '7', '6', '6', '5', '4', '7', '5', '5', '6', 5.6, '0.9', '5.6±0.9', '5.5'],
    ]

    table_1 = [
        ['15', '13', '14', '16', '15', '17', '16', '13', '14', '15', 14.8, '1.2', '10.4', '0.3'],
    ]
    Memory = {
        'newsavename': '',
        'h': '1',
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
    return MemoryField


def SetMemoryField(field, value):
    global mem
    mem[f'{field}'] = value
