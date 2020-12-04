def part1(g): #thanks to my man Andrew for pointing out that the pattern goes on indefinitely in the horizontal pos
    treecount = 0
    total = 1
    pos_x = 0
    pos_y = 0
    
    while pos_y < len(g):
        if g[pos_y][pos_x] == "#":
            treecount+=1
        pos_x+=3
        if pos_x >= 31: #check to see if we have to repeat, use good old modulus
            pos_x %= 31
        pos_y+=1  
    print(treecount) 
 
def part2(g):
    '''
    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.). Dont need to calculate this. 244
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.
    '''
    #im going to redo the one I calculated just because I want to see a list of everything
    treecount = [0,0,0,0,0]
    pos_arr = [[0,0],[0,0],[0,0],[0,0],[0,0]]
    mov_lst = [[1,1],[3,1],[5,1],[7,1],[1,2]] #remember sub_0 is x, sub_1 is y 
    depth = len(g)
    #c_tree = 0
    for i in range(len(pos_arr)):
        print(i)
        while pos_arr[i][0] < depth:

            if g[pos_arr[i][0]][pos_arr[i][1]] == '#':
                treecount[i]+=1
            pos_arr[i][1]+=mov_lst[i][0]
            if pos_arr[i][1] >= 31:
                pos_arr[i][1]%=31
            pos_arr[i][0]+=mov_lst[i][1]
    print(treecount)
    product = 1
    for i in range(len(treecount)):
        product*=treecount[i]
    print(product)
        




f = open("input.txt")
g = [line.strip() for line in f.readlines()]
part2(g)

f.close()