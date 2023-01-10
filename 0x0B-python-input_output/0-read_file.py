#!/usr/bin/python3
def read_file(filename=""):
    with open("myfile.txt", mode="r", encoding="utf8") as file:
        print(file.read())
