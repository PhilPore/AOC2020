

def firstnonsum(g,preamb): #a better approach could have been a tree sort, a normal queue like array wil ldo
    #preamb.sort()
    lookup = {}
    for i in preamb:
        lookup[i] = 1
    val = 0
    for i in range(25,len(g)):
        val = int(g[i].strip())
        pre_count = 25
        while pre_count > 0:
            if (val-preamb[pre_count-1]) in lookup.keys() and val-preamb[pre_count-1] != preamb:
                break
            pre_count-=1
        if pre_count == 0:
            print(val)
            print(i)
            return val
        lookup.pop(preamb[0],None)
        preamb.pop(0)
        preamb.append(val)
        lookup[val] = 1
        
def findencryptbase(listarr,sum_val): 
    #you were a monkey and clearing everything rather than popping the first part of the queue 
    #fix tomorrow
    sumof = 0
    subed_ptr,substrt_ptr = len(listarr)-1,len(listarr)-1
    subqueue = []
    while subed_ptr > 0:

        if listarr[subed_ptr] >= sum_val:
            
            subed_ptr-=1
            sumof = 0
            subqueue.clear()
            continue
        sumof+=listarr[subed_ptr]
        subqueue.append(listarr[subed_ptr])
        if sumof > sum_val:
            #print("{} {}".format(sumof, subqueue[0]))
            sumof-=subqueue.pop(0)
            
        if sumof == sum_val:
            #print("Rap")
            print(min(subqueue)+max(subqueue))
        subed_ptr-=1
    
  
        



        
    

#part 2, work backwords. From the end of the list up
f = open("input.txt")
g = f.readlines()
preamble = [int(g[i].strip()) for i in range(25)]
genlist = [int(g[i].strip()) for i in range(len(g))]

x= firstnonsum(g,preamble)
findencryptbase(genlist,x)