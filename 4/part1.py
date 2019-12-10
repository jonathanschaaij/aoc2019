count = 0

for code in range(248345,746315):

    double = False
    in_a_row = 1
    good = True
    print(code)
    for nr in range(1,6):
        if int(str(code)[nr]) < int(str(code)[nr-1]):
            good = False
            break
        row_value = str(code)[nr-1]
        if str(code)[nr] == str(code)[nr-1]:
            in_a_row +=1
            print(in_a_row,'found something', str(code)[nr])
        else:
            in_a_row = 1

        if in_a_row == 2:
            if double == False: double_value = str(code)[nr]
            double = True
        elif in_a_row > 2 and double_value == str(code)[nr]:
            double = False



    if double and good:
        print(code)
        count +=1

print(count)
