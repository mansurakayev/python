import os
def file_read(name):
        txt = open(name)
        print(txt.read())
file_read('Test1.txt')