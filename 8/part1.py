import input


layers =[]
for x in range(0,len(str(input.data)), 150): #150 characters per layer
    layers.append(str(input.data)[x:x+150])


best_zeros = 150;
for layer in range(len(layers)):
    zeros = 0
    for char in layers[layer]:
        if char == '0':
            zeros += 1
    if zeros < best_zeros:
        best_zeros = zeros
        best_layer = layer
        # print(zeros, best_layer)

for i in range(0,len(layers[best_layer]), 25):
    print(layers[best_layer][i:i+25])



ones = 0
twos = 0
for char in layers[best_layer]:
    if char == '1':
        ones +=1
    if char == '2':
        twos += 1

print(ones, twos, ones*twos)
