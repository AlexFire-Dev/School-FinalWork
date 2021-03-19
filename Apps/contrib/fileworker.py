import os


for file in os.listdir('Saves/'):
    if file.endswith('.json'):
        print(file)
