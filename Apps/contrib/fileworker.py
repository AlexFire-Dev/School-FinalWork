import os
import json

from Apps.contrib.control import *


def GetSaves():
    Saves = []
    for file in os.listdir('Saves/'):
        if file.endswith('.json'):
            Saves.append(file)
    return Saves


def LoadSave(file):
    with open(f'Saves/{file}', 'r') as read_file:
        SetMemory(json.load(read_file))
    print(GetMemory())
