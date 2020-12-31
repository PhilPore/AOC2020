def makeclust(parsestring):
    parsedic={}
    for i in parsestring:
        if i not in parsedic:
            parsedic[i] = 1
        else:
            parsedic[i]+=1
    return parsedic


def part1(g):
    answrstring=""
    helpsum = 0
    for line in g:
        if line[0] == '\n' or line == g[-1]:
            helpsum+=len(makeclust(answrstring))
            answrstring=""
        else:   
            answrstring+=line.strip()
    print(answrstring)
    print(helpsum)
    #print(helpsum+len(makeclust(answrstring))) was here because i decided to not add that or statement initially
    
def part2(g):
    answrstring=""
    answsum=0
    groupmems = 0
    for line in g:
        if line[0] == '\n' or line == g[-1]:
            parsedic = makeclust(answrstring)
            for i in parsedic:
                answsum+=1 if parsedic[i] == groupmems else 0
            answrstring=""
            groupmems = 0
            
            
        else:
            answrstring+=line.strip()
            groupmems+=1
    print(answsum)


fle = open("input.txt")
g = fle.readlines()

part2(g)