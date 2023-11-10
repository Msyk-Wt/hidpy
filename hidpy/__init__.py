import os

def hello():
    path = os.path.dirname(__file__) + '\\default.txt'
    with open(path) as file:
        text = file.read()
        print(text)
