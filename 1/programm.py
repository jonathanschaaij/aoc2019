import math
file = open('input.txt')
lines = [line.rstrip('\n') for line in file]

fuel = 0;
for m_mod in lines:
    f_mod = math.floor(int(m_mod)/3)-2;
    f_fuel = f_mod
    while f_fuel > 0:
        f_fuel = math.floor(f_fuel/3)-2;
        if f_fuel > 0:
            f_mod += f_fuel
    fuel += f_mod

print(fuel)
