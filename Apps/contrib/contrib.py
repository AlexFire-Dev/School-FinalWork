import datetime
import json


def StartSession():
    file = open('logfile.txt', 'a')
    now = datetime.datetime.now()
    now = str(now)[:-7]
    print(f'----{now}----')
    print(f'----{now}----', file=file)
    file.close()


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


def PrintDictionary(dictionary, indent=4, name=''):
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
