import csv
import random

n = int(input('le nombre de province a creer: '))

color = []

default = ["land", "false", "plains", "0"]

with open("definition.csv") as file:
    t = csv.reader(file, delimiter=';')
    for i in t:
        color.append([i[1],i[2],i[3]])

with open("definition.csv", "a") as file:
    for i in range(n):
        new_color = [str(random.randint(0,255)),str(random.randint(0,255)),str(random.randint(0,255))]
        while new_color in color:
            new_color = [str(random.randint(0,255)),str(random.randint(0,255)),str(random.randint(0,255))]
        l = [str(len(color)+i)]+new_color+ default
        s = "".join(j+";" for j in l)+"\n"
        file.write(s)