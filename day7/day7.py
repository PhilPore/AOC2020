import string
class node:

    def __init__(self,bagtype,bagamount):
        self.bagtype = bagtype.translate(str.maketrans('', '', string.punctuation))
        if self.bagtype[-1] == 'g':
            self.bagtype+='s'
        self.bagamount = bagamount
    def getname(self):
        return self.bagtype
    def getbagamount(self):
        return self.bagamount
    

def findgoldbags(grph):
    counter = 0
    searchcount=0
    hasgold={}
    #print(grph.keys())
    for bag in grph:

        if bag == "shiny gold bags":
            continue
        #print(bag)
        #print("--")
        for edge in grph[bag]:
            
            if edge == None:
                break
            comp = edge.bagtype
            #print(comp, end=" ")
            if comp in hasgold:
                counter+=1
                
                break
            explored =[]
            pos = comp
            frontier=[]
            frontier.append(comp)
            found = 0
            searchcount+=1
            while(len(frontier) > 0):

                nde = frontier.pop(0)

                if nde not in explored:
                    if nde == "shiny gold bags":
                        found = 1
                        hasgold[comp] = True
                        counter+=1
                        print(comp)
                        break
                    elif nde in hasgold:
                        found = 1
                        counter+=1
                        print(comp)
                        break
                    else:
                        for element in grph[nde]:
                            if element != None:
                                frontier.append(element.bagtype)
                            else:
                                frontier.append(None)
                                explored.append(None)
                explored.append(nde)
                if found == 1:
                    break
            if found == 1: 
                break
    print(counter)
    print(searchcount)

def whatsinthebag(grph): # need to look at this again, figure out the math
    x ="shiny gold bags" 
    y = whatsinbagrecurse(x,grph)
    print(y)
    return y


def whatsinbagrecurse(name,graph):
    counter = 0
    #print(name)
    for i in graph[name]:
        if i == None:
            return 0
        
        counter+= i.bagamount + i.bagamount*whatsinbagrecurse(i.bagtype,graph)
    #if name == "shiny gold bags":
        #print(counter)
    #print("I'm literally about to return this god forsaken variable")
    return counter
    

def countgoldbetter(grph,mp):
    return 0
    
fle = open("input.txt")
g=fle.readlines()
adjlist = {}
for line in g:
    adjname = line.split("contain")[0].strip()
    prse = line.split("contain")[1].split(",")

    #print("{} | {}".format(adjname,prse))
    if adjname not in adjlist:
        adjlist[adjname] = [] 
    
    #prse = line.split("contain")[1].split(",")
    for i in range(len(prse)):
        par = prse[i]
        if par.strip().split()[0] != "no":
            ins_int = int(par.strip().split()[0])
            ins_str= par.strip()[2:]
            check = node(ins_str,ins_int)
            adjlist[adjname].append(check)
            #print(check.bagtype)
            #print(check.bagamount)
        else:
            #print("Nill")
            adjlist[adjname].append(None)

#findgoldbags(adjlist)
x = whatsinthebag(adjlist)
#print(x)    