import re

with open("input\\day20.txt", 'r') as f:
    for i, line in enumerate(f):
        acc = tuple(map(int, re.findall("a=<(-*[0-9]+),(-*[0-9]+),(-*[0-9]+)>", line)[0]))
        acc_norm = abs(acc[0]) + abs(acc[1]) + (abs(acc[2]))
        if acc_norm == 1:
            vel = tuple(map(int, re.findall("v=<(-*[0-9]+),(-*[0-9]+),(-*[0-9]+)>", line)[0]))
            vel_norm = abs(vel[0]) + abs(vel[1]) + (abs(vel[2]))
            print(vel_norm, line, i)

"""
?
?
?
"""