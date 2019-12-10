file = open('input.txt')
lines = [line.rstrip('\n') for line in file]

lines = """COM)BBB
BBB)CBB
CBB)DBB
DBB)EBB
EBB)FBB
BBB)GBB
GBB)HBB
DBB)IBB
EBB)JBB
JBB)KBB
KBB)LBB
KBB)YOU
IBB)SAN""".split('\n')

orbit={

}

for line in lines:
    object = line.split(')')
    for x in object:
        if x not in orbit:
            orbit[x]='0'
    orbit[object[1]] = object[0]

total = 0


for planet in orbit:
    object = planet
    n=0
    while not orbit[object] == '0':
        n+=1
        object  = orbit[object]

    total += n

print(total)
