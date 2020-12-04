

f = open("input.txt")

g = f.readlines()
dic = {}
arr = []
comp = 2020
print(len(g))
#build it up
for i in g:
    x = int(i)
    print(x)
    arr.append(x)
    dic[x] = 1
    
print(len(dic))
#part 1
for i in dic:
    if (comp-i) in dic:
        print((comp-i)*i)
        break
#part 2
for j in range(len(arr)):
    
    for q in range(len(arr)):
        if q == j:
            continue
        if comp-(arr[j]+arr[q]) in dic:
            print((comp-(arr[j]+arr[q]))*arr[j]*arr[q])
            break

f.close()