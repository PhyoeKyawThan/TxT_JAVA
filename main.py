#!/usr/bin/python3
from transform import Generator
from os import system

helloWorld = Generator("HelloWorld")
with open("commands.txt", "r") as commands:
    commands = commands.readlines()
codes = ""
for command in commands:
    if command[0:3] == "out":
        codes += f"System.out.print({command[4:-1]});\n"
codes = codes[:-1]
helloWorld.codes_generate("HelloWorld.java", codes)

system("javac HelloWorld.java")
system("java HelloWorld")
