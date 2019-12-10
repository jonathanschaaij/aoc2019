print("Advent Of Code Day 07")

computer_default_instructions=[3,8,1001,8,10,8,105,1,0,0,21,42,67,88,101,114,195,276,357,438,99999,3,9,101,3,9,9,1002,9,4,9,1001,9,5,9,102,4,9,9,4,9,99,3,9,1001,9,3,9,1002,9,2,9,101,2,9,9,102,2,9,9,1001,9,5,9,4,9,99,3,9,102,4,9,9,1001,9,3,9,102,4,9,9,101,4,9,9,4,9,99,3,9,101,2,9,9,1002,9,3,9,4,9,99,3,9,101,4,9,9,1002,9,5,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,99]

# computer_default_instructions = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
# computer_default_instructions = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
# computer_default_instructions = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]


def getParameterMode(command_pos, computer):
    command = str(computer[command_pos])
    param = [0,0]
    try:
        param[0] = int(command[-3])
    except:
        param[0]= 0
    try:
        param[1] = int(command[-4])
    except:
        param[1] = 0
    return param

def getParameter(command_pos, computer):
    param = getParameterMode(command_pos, computer)
    a = computer[command_pos+1] if param[0] else computer[computer[command_pos+1]]
    b = computer[command_pos+2] if param[1] else computer[computer[command_pos+2]]

    return [a,b]

def compute(phase, input):
    n=0
    computer = computer_default_instructions.copy()
    command_pos = 0
    while True:
        command = str(computer[command_pos])
        opcode =  int(command[-2:])


        if opcode == 99:
            break
        elif opcode == 1:
            para = getParameter(command_pos, computer)
            computer[computer[command_pos+3]] = para[0]+para[1]
            step = 4
        elif opcode == 2:
            para = getParameter(command_pos, computer)
            computer[computer[command_pos+3]] = para[0]*para[1]
            step = 4
        elif opcode == 3:
            computer[computer[command_pos+1]] = input if n==1 else phase
            n+=1
            step = 2
        elif opcode == 4:
            param = getParameterMode(command_pos, computer)
            output = computer[command_pos+1] if param[0] else computer[computer[command_pos+1]]
            # print("The output is: ",output)
            step = 2
        elif opcode == 5:
            para = getParameter(command_pos, computer)
            if para[0]:
                command_pos = para[1]
                continue
            else:
                step = 3
        elif opcode == 6:
            para = getParameter(command_pos, computer)
            if not para[0]:
                command_pos = para[1]
                continue
            else:
                step = 3
        elif opcode == 7:
            para = getParameter(command_pos, computer)
            computer[computer[command_pos+3]] =1 if para[0]<para[1] else 0
            step = 4
        elif opcode == 8:
            para = getParameter(command_pos, computer)
            computer[computer[command_pos+3]] =1 if para[0]==para[1] else 0
            step = 4
        else:
            print("Something has gone wrong")
            break
        command_pos += step
    return output


max = 0
best_phase = [0,0,0,0,0]
for A in range(5):
    for B in range(5):
        if B == A:
            continue
        for C in range(5):
            if C == A or C == B:
                continue
            for D in range(5):
                if D == C or D == B or D == A:
                    continue
                E = 10 - A-B-C-D
                input = 0
                phases = [A,B,C,D,E]
                for x in phases:
                    output = compute(x, input)
                    input = output
                if input > max:
                    max = input
                    best_phase = phases

print("Max Signal: ",max)
print("Phase: ", best_phase)
