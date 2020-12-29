
#for the first seven
#f = upper half
#b = lower half

#for the last 3
#r = upper half
#l = lower half

def part1(g,o_e,o_s):
    
    maxboy = 0
    for lines in g:
        e = o_e
        s = o_s
        area = e-s
        nval = 0
        for i in range(7):
            
            if lines[i] == 'F':
                
                    
                e -= area//2+1
                
                area = e-s
                
                nval = e    
            else:
                
                s += area//2+1
                area = e-s
                nval = s
            
        nval*=8
        tmpval = 0
        row_s = 0
        row_e = 7
        row_area = row_e - row_s
        
        for i in range(7,10):
            if lines[i] == 'R': #upper half
            # print("R:")
                row_s+=row_area//2+1
                #print(row_s)
                row_area = row_e-row_s
                #print(row_area)
                tmpval = row_s
            else:
                row_e-=row_area//2+1
                row_area = row_e-row_s
                tmpval = row_e
        maxboy = max(maxboy, nval+tmpval)
    return maxboy

def part2(g,o_e,o_s): #build a list and sort it. Find the values next to each other that are 2 apart. That will be your seat.
    maxboy = []
    for lines in g:
        e = o_e
        s = o_s
        area = e-s
        nval = 0
        for i in range(7):
            
            if lines[i] == 'F':
                
                    
                e -= area//2+1
                
                area = e-s
                
                nval = e    
            else:
                
                s += area//2+1
                area = e-s
                nval = s
            
        nval*=8
        tmpval = 0
        row_s = 0
        row_e = 7
        row_area = row_e - row_s
        
        for i in range(7,10):
            if lines[i] == 'R': #upper half
            # print("R:")
                row_s+=row_area//2+1
                #print(row_s)
                row_area = row_e-row_s
                #print(row_area)
                tmpval = row_s
            else:
                row_e-=row_area//2+1
                row_area = row_e-row_s
                tmpval = row_e
        ins = tmpval+nval
        maxboy.append(ins)
    maxboy.sort()
    myid = 0
    for i in range(1,len(maxboy)-1):
        if maxboy[i+1]-maxboy[i] == 2:
            myid = maxboy[i]+1
            break 
    return myid



fle = open("input.txt")
e = 127
s = 0
g = fle.readlines()
maxid = part1(g,e,s)
print(maxid)
output = part2(g,e,s)
print(output)


