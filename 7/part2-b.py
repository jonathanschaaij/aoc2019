print("Advent Of Code Day 05")
computer_default_instructions=[3,8,1001,8,10,8,105,1,0,0,21,42,67,88,101,114,195,276,357,438,99999,3,9,101,3,9,9,1002,9,4,9,1001,9,5,9,102,4,9,9,4,9,99,3,9,1001,9,3,9,1002,9,2,9,101,2,9,9,102,2,9,9,1001,9,5,9,4,9,99,3,9,102,4,9,9,1001,9,3,9,102,4,9,9,101,4,9,9,4,9,99,3,9,101,2,9,9,1002,9,3,9,4,9,99,3,9,101,4,9,9,1002,9,5,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,99]

# computer_default_instructions = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
# computer_default_instructions =[3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]

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

def compute(phase):
    amp_com = []
    command_pos_amps = []
    getPhase = []
    for x in range(5):
        amp_com.append(computer_default_instructions.copy())
        command_pos_amps.append(0)
        getPhase.append(True)


    amp = 0
    input = 0
    n=0
    while True:
        command_pos = command_pos_amps[amp]
        computer = amp_com[amp]
        command = str(computer[command_pos])
        opcode =  int(command[-2:])
        # print(command_pos)
        # print("Opcode: ", opcode)

        if opcode == 99:
            break
        elif opcode == 1: #ADD
            para = getParameter(command_pos, computer)
            computer[computer[command_pos+3]] = para[0]+para[1]
            step = 4
            # print("Opcode 1: Add ", para)
        elif opcode == 2: #Multiply
            para = getParameter(command_pos, computer)
            computer[computer[command_pos+3]] = para[0]*para[1]
            step = 4
            # print("Opcode 2: Multiply ", para)
        elif opcode == 3: #Input
            answer =  phase[amp] if getPhase[amp] else input
            computer[computer[command_pos+1]] = answer
            # print("Received input", answer, getPhase[amp])
            getPhase[amp] = False
            step = 2
        elif opcode == 4: #Output
            param = getParameterMode(command_pos, computer)
            output = computer[command_pos+1] if param[0] else computer[computer[command_pos+1]]
            # print("The output is: ",output)
            input = output
            step = 2
            command_pos_amps[amp] += step
            amp = amp+1 if amp < 4  else 0
            # print("switched to amp: ", amp)
            continue
        elif opcode == 5: #Jump if true
            para = getParameter(command_pos, computer)
            # print("Opcode 5; Para ", para)
            if para[0]:
                command_pos_amps[amp] = para[1]
                # print("Opcode 5: Jumped to ", para[1])
                continue
            else:
                # print("Opcode 5: Didn't Jump")
                step = 3
        elif opcode == 6: #jump if false
            para = getParameter(command_pos, computer)
            if not para[0]:
                print("Opcode 6; Jumped to: ",para[1])
                command_pos = para[1]
                continue
            else:
                print("Opcode 6; Didn't Jump")
                step = 3
        elif opcode == 7: #Less than
            para = getParameter(command_pos, computer)
            computer[computer[command_pos+3]] =1 if para[0]<para[1] else 0

            step = 4
        elif opcode == 8: #Equals
            para = getParameter(command_pos, computer)
            computer[computer[command_pos+3]] =1 if para[0]==para[1] else 0
            step = 4
        else:
            print("Something has gone wrong")
            break
        amp_com[amp]=computer
        command_pos_amps[amp] += step
    return output
    print("The final output is: ", output)

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
                input = compute(phases)
                if input > max:
                    max = input
                    best_phase = phases

print("Max Signal: ",max)
print("Phase: ", best_phase)
