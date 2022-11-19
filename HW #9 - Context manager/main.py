from datetime import datetime
import csv
import json
#Створити логер який дозволяє працювати з файлами як звичайний open,
# але разом з тим в файл logs.txt записує:
# коли був відкритий файл, назва файла, коли закритий файл

class MyCustomManager:
    def __init__(self, file_name, mode):
        self.file_name = file_name
        MyCustomManager.write_log_file(self.file_name, "OPEN \n")
        self.file = open(file_name, mode)

    def __enter__(self):
        return self.file

    def __exit__(self, type, value, traceback):
        self.file.close()
        MyCustomManager.write_log_file(self.file_name, "CLOSE \n")

    @classmethod
    def write_log_file(cls, name_file, action):
        cls.name_file = name_file
        cls.action = action
        with open('logs.txt', 'a') as log:
            log.write(f'{datetime.now()} {name_file} {action}')


with MyCustomManager('file.txt', 'r') as open_file:
    print(open_file.read())

#Написати ф-цію яка переводить файл logs.txt в logs.csv

def writer():
    file = open("logs.txt")
    with open('logs.csv', 'w') as csv_file:
        for line in file:
            csv_file.write(line.strip('/n'))

writer()

