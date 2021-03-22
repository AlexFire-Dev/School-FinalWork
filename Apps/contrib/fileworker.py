import os
import json

from Apps.contrib.control import *


# Получает список всех сохранений
def GetSaves():
    Saves = []
    for file in os.listdir('Saves/'):
        if file.endswith('.json'):
            Saves.append(file)
    return Saves


# Получает данные из сохранения
def LoadSave(file):
    with open(f'Saves/{file}', 'r') as read_file:
        SetMemory(json.load(read_file))
    print(GetMemory())


# Создает сохранение
def CreateNewSave(filename):
    if f'{filename}.json' in GetSaves():
        return 1
    elif len(GetMemoryField('newsavename')) == 0:
        return 2
    else:
        with open(f'Saves/{filename}.json', 'w') as write_file:
            json.dump(GetMemory(), write_file, indent=4)
        return 0


# Удаляет сохранение
def DeleteSave(file):
    os.remove(f'Saves/{file}')


# Пересоздает сохранение
def ReCreate(file):
    DeleteSave(file)
    with open(f'Saves/{file}', 'w') as write_file:
        json.dump(GetMemory(), write_file, indent=4)
