file = open('input.txt')
lines = [line.rstrip('\n') for line in file]

# lines = """COM)BBB
# BBB)CBB
# CBB)DBB
# DBB)EBB
# EBB)FBB
# BBB)GBB
# GBB)HBB
# DBB)IBB
# EBB)JBB
# JBB)KBB
# KBB)LBB
# KBB)YOU
# IBB)SAN""".split('\n')

orbit={

}

for line in lines:
    object = line.split(')')
    for x in object:
        if x not in orbit:
            orbit[x]=''
    orbit[object[1]] = object[0]

total = 0


for planet in orbit:
    object = planet
    while not orbit[object] == '':
        object = orbit[object][0:3]
        orbit[planet] += orbit[object][0:3]
    n = len(orbit[planet])//3
    total += n

#determine overlap
k = -3
while orbit['YOU'][k:] == orbit['SAN'][k:]:
    k -= 3

k+=6

distance = len(orbit['YOU'])//3 + len(orbit['SAN'])//3 + 2*k//3 -2

print("Distance YOU --> SAN : ", distance)
