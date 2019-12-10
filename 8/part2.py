import input

layers =[]
for x in range(0,len(str(input.data)), 150): #150 characters per layer
    layers.append(str(input.data)[x:x+150])

picture = []
for i in range(0,150):
    picture.append('?')


for i in range(150):
    for x in layers:
        if str(x[i]) == '0' and picture[i] == '?':
            picture[i] = '  '
        if str(x[i]) == '1' and picture[i] == '?':
            picture[i] = '██'



for i in range(0,len(picture), 25):
    print(''.join(picture[i:i+25]))
