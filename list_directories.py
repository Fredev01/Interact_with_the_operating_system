import os

pwd: str = os.getcwd()
list_directory: list = os.listdir(pwd)

for directory in list_directory:
    print('[+]', directory)
