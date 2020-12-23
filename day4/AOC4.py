import string

'''
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
Passport data is validated in batch files (your puzzle input). 
Each passport is represented as a sequence of key:value pairs separated by spaces or newlines. 
Passports are separated by blank lines.


Missing cid is fine, but missing any other field is not, so this passport is invalid.
'''
def validate1(dic_arr):
    if len(dic_arr) == 8 or (len(dic_arr ) == 7 and "cid" not in dic_arr):
        return 1
    return 0


'''
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
'''

def validate2(dic_arr):
    if len(dic_arr) == 8 or (len(dic_arr ) == 7 and "cid" not in dic_arr):
        #validate. Series of checks.
        #validate byr, eyr, iyr first
        if ((int(dic_arr['byr']) >= 1920 and int(dic_arr['byr']) <= 2002) and 
        (int(dic_arr['iyr']) >= 2010 and int(dic_arr['iyr']) <= 2020) and 
        ((int(dic_arr['eyr']) >= 2020 and int(dic_arr['eyr']) <= 2030))):
           # print("seems valid!")
            #validate hght
            if("cm" in dic_arr['hgt']):
                if (int(dic_arr['hgt'][:-2]) < 150 or int(dic_arr['hgt'][:-2]) > 193):
                    return 0
            elif("in" in dic_arr['hgt']):
                #print(dic_arr['hgt'][:-2])
                if (int(dic_arr['hgt'][:-2]) < 59 or int(dic_arr['hgt'][:-2]) > 76):
                    #print("EEEE")
                    return 0
            else:
                return 0


            #validate hair color hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f
            if dic_arr['hcl'][0] == '#' and len(dic_arr['hcl'][1:]) == 6 and dic_arr['hcl'][1:].isalnum():
                #validate eye color exactly one of: amb blu brn gry grn hzl oth.
                if len(dic_arr['ecl']) == 3 and dic_arr['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth']:
                    if len(dic_arr['pid']) == 9:
                        #print(dic_arr)
                        return 1

            #validate pid
        else:
            return 0
    return 0
f = open("input.txt")
h = f.readlines()
#dic_array =[] #holds all valid records
#print(clusters)
clust_ind = 0
preroc = ""
valid = 0
for line in range(len(h)):
    #print(line)
    if h[line] != "\n":
        preroc+=h[line].strip()+" "
    if h[line] == "\n"  or line == len(h)-1:
        x =[i.split(":") for i in preroc.split()]
        dic = {}
        for j in x:
            dic[j[0]] = j[1]

        #print(dic)
        #valid+=validate1(dic)
        #print(dic)
        valid+=validate2(dic)
        preroc =""
    

print(valid)


