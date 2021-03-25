import datetime


# Стартовая надпись в консоль
def StartSession():
    file = open('logfile.txt', 'a')
    now = datetime.datetime.now()
    now = str(now)[:-7]
    print(f'----{now}----')
    print(f'----{now}----', file=file)
    file.close()


# Лог в консоль
def log(*args, **kwargs):
    file = open('logfile.txt', 'a')
    print('    log', end=': ')
    print('    log', end=': ', file=file)
    if kwargs.get('way', None):
        for way in kwargs.get('way'):
            print(way, end=': ')
            print(way, end=': ', file=file)
    for arg in args:
        print(arg, end=' ')
        print(arg, end=' ', file=file)
    print()
    print(file=file)
    file.close()


# Ошибка в консоль
def exception(*args, **kwargs):
    file = open('logfile.txt', 'a')
    print('    exception', end=': ')
    print('    exception', end=': ', file=file)
    if kwargs.get('way', None):
        for way in kwargs.get('way'):
            print(way, end=': ')
            print(way, end=': ', file=file)
    for arg in args:
        print(arg, end=' ')
        print(arg, end=' ', file=file)
    print()
    print(file=file)
    file.close()


# Счетчик производительности
def PerfCheck(func=None, name=None, args=None, kwargs=None):
    file = open('logfile.txt', 'a')
    print('    ------------')
    print('    ------------', file=file)
    print(f'    {name} Console:\n')
    print(f'    {name} Console:\n', file=file)
    file.close()
    start = datetime.datetime.now()
    if args and kwargs:
        func(*args, **kwargs)
    elif args:
        func(*args)
    elif kwargs:
        func(**kwargs)
    else:
        func()
    end = datetime.datetime.now()
    timeSec = end.second - start.second
    timeMic = end.microsecond - start.microsecond
    file = open('logfile.txt', 'a')
    print(f'\n    PerfCheck {timeSec}:{timeMic}')
    print(f'\n    PerfCheck {timeSec}:{timeMic}', file=file)
    print('    ------------')
    print('    ------------', file=file)
    file.close()


# Словарь в консоль
def PrintDictionary(dictionary, indent=6, name=''):
    file = open('logfile.txt', 'a')
    print('    ------------')
    print('    ------------', file=file)
    print(f'    Dictionary {name}:\n')
    print(f'    Dictionary {name}:\n', file=file)
    for line in dictionary.keys():
        try:
            indent = (int(indent)*' ')
        except ValueError:
            pass
        ClassType = str(type(dictionary.get(line, '')))
        ClassType = ClassType[8:-2]
        if ClassType == 'str' or ClassType == 'int' or ClassType == 'float':
            print(indent, f'{line}: ', dictionary.get(line, ''), sep='')
            print(indent, f'{line}: ', dictionary.get(line, ''), sep='', file=file)
        elif ClassType == 'list':
            Name = f'{line}: ['
            print(indent, Name, sep='')
            print(indent, Name, sep='', file=file)
            for arg in dictionary.get(line, ''):
                print(indent, indent, len(Name)*' ', arg, ',', sep='')
                print(indent, indent, len(Name)*' ', arg, ',', sep='', file=file)
            print(indent, (len(Name)-1)*' ', ']', sep='')
            print(indent, (len(Name)-1)*' ', ']', sep='', file=file)
        elif ClassType == 'dict':
            Name = f'{line}:' + ' {'
            print(indent, Name, sep='')
            print(indent, Name, sep='', file=file)
            for value in dictionary.get(line, '').keys():
                print(indent, indent, len(Name)*' ', value, ': ', dictionary.get(line, '').get(value, ''), ',', sep='')
                print(indent, indent, len(Name)*' ', value, ': ', dictionary.get(line, '').get(value, ''), ',', sep='', file=file)
            print(indent, (len(Name)-1)*' ', '}', sep='')
            print(indent, (len(Name)-1)*' ', '}', sep='', file=file)
    print('    ------------')
    print('    ------------', file=file)
    file.close()
