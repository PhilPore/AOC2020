import copy
def beforerepeat(instrct):
    acc = 0
    i = 0
    while(i<len(instrct)):
        incr = 0
        if instrct[i][-1] == 1:
            break
        if instrct[i][0] == "nop":
            incr+=1
        elif instrct[i][0] == "acc":
            incr+=1
            
            acc+=instrct[i][1]
            
        elif instrct[i][0] == "jmp":   
            incr+=instrct[i][1]
            
        instrct[i][-1] = 1
        i+=incr
    print(acc) 
def shouldchange(instrct, pos):
    temp_pos = pos
    temp_instrct = copy.deepcopy(instrct)
    if instrct[pos][0] == "nop": #turn to jmp
        temp_pos+=instrct[pos][1]
    else:
        temp_pos+=1
    while temp_pos < len(temp_instrct):
        if temp_instrct[temp_pos][-1] == 1:
            return False
        temp_instrct[temp_pos][-1] = 1
        if temp_instrct[temp_pos][0] == "nop":
            temp_pos+=1
        elif temp_instrct[temp_pos][0] == "jmp":
             temp_pos+=instrct[temp_pos][1]
        else:
            temp_pos+=1
    return True
def modinstr(instrct):
    notchanged = True
    i = 0
    acc = 0
    prev = []
    while(i < len(instrct)):
        incr = 0
        #print(instrct[i])
        if instrct[i][-1] == 1:
            print("found repeat at {} | {} from {}".format(i,instrct[i],prev))
            break
        instrct[i][-1] = 1
        if instrct[i][0] == "nop":
            #print("in nop {} | {}".format(i,instrct[i]))
            if shouldchange(instrct,i) and notchanged:
                print("Changing nop {} {} to jmp".format(i , instrct[i]))
                incr+=instrct[i][1]
                notchanged = False
            else:    
                incr+=1
            prev = [i,instrct[i]]
        elif instrct[i][0] == "jmp":
            #print("In jmp {}|{}".format(i,instrct[i]))
            if shouldchange(instrct,i) and notchanged:
                print("Changing jmp {} {} to nop".format(i , instrct[i]))
                incr+=1
                notchanged = False
            else:
                incr+=instrct[i][1] 
            prev = [i,instrct[i]]
        elif instrct[i][0] == "acc":
            acc+= instrct[i][1] 
            incr+=1
        i+=incr
    print(acc)

            


f = open("input.txt")

g = f.readlines()
instruct_stream = []

for line in g: #format data
    instruct = line.split()[0]
    #instruct_dir = line.split()[1][0].strip()
    instruct_num = int(line.split()[1][1:].strip()) if line.split()[1][0].strip() == '+' else -int(line.split()[1][1:].strip())
    instruct_stream.append([instruct,instruct_num,0])

modinstr(instruct_stream)
#for i in range(len(instruct_stream)):
    #print("{} | {}".format(i,instruct_stream[i]))
#beforerepeat(instruct_stream)
f.close()