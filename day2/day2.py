
def part1(g): #part 1. THE CLERK LIED TO USE MAN WHAT THE HELL.
    count = 0
    for line in g:
        x = line
        xsub = line.split(":")
        xsubi = xsub[0].split(" ")[0].split("-")

        if xsub[1].count(xsub[0][-1]) >= int(xsubi[0]) and xsub[1].count(xsub[0][-1]) <= int(xsubi[1]):
            count+=1
    print(count)

def part2(g): #part 2
    count = 0
    for line in g:
        x = line
        xsub = line.split(":")
        xsubi = xsub[0].split(" ")[0].split("-")
        xsubi = [int(xsubi[0]),int(xsubi[1])]
        # search. Remember, exactly one of these positions need to have one. So we need to do a check
        target = xsub[0][-1]
        seek = xsub[1].split()[0]
        count+= (target == seek[xsubi[0]-1]) ^ (target == seek[xsubi[1]-1])
        ''' 
        this was what I used previously but the XOR operation makes it far cleaner.
       if target == seek[xsubi[0]-1] and target == seek[xsubi[1]-1]:
            continue
        elif target == seek[xsubi[0]-1]:
            count+=1
        elif target == seek[xsubi[1]-1]:
            count+=1 
        '''
    print(count)
      
        


f = open("input.txt")
g = f.readlines()
h = g[0].split(":")
part2(g)

f.close()