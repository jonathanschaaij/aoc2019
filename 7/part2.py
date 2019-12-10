print("Advent Of Code Day 07")

computer_default_instructions=[3,8,1001,8,10,8,105,1,0,0,21,42,67,88,101,114,195,276,357,438,99999,3,9,101,3,9,9,1002,9,4,9,1001,9,5,9,102,4,9,9,4,9,99,3,9,1001,9,3,9,1002,9,2,9,101,2,9,9,102,2,9,9,1001,9,5,9,4,9,99,3,9,102,4,9,9,1001,9,3,9,102,4,9,9,101,4,9,9,4,9,99,3,9,101,2,9,9,1002,9,3,9,4,9,99,3,9,101,4,9,9,1002,9,5,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,99]

computer_default_instructions = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
computer_default_instructions =[3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]

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

def compute(phase, input, computers, amp_command_pos):
    amp_nr = 0
    input_phase = [True,True,True,True,True]
    while True:
        computer = computers[amp_nr]
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
            computer[computer[command_pos+1]] = input if not input_phase[amp_nr] else phase
            input_phase[amp_nr] = False
            step = 2
        elif opcode == 4:
            param = getParameterMode(command_pos, computer)
            output = computer[command_pos+1] if param[0] else computer[computer[command_pos+1]]
            print("The output is: ",output)
            input = output
            step = 2
            amp_nr = amp_nr + 1 if amp_nr < 4 else 0
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

def run_phase(phase):
    global max
    input = 0
    print("Phase in Testing: ", phases)
    for x in range(5):
        amp[x] = computer_default_instructions.copy()
        command_pos[x] = 0

    compute(phase, input, amp, command_pos)

    if input > max:
        max = input
        best_phase = phases

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
                phases = [A+5,B+5,C+5,D+5,E+5]
                run_phase(phases)


print("Max Signal: ",max)
print("Phase: ", best_phase)
