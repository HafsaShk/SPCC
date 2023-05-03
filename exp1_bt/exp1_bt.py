with open('pg1_input.txt') as t:
    data = []
    for line in t.readlines():
        data.append(line.split())
#print(data)

symbols = []
value = 0
def contains(string):
    string = list(string)
    for i in string:
        if i == "F":
            return 4
        elif i =="D":
            return 8
    return 1

def contains_literal(string):
    string = list(string)
    if "=" in string:
        return True

for j, i in enumerate(data):
    
    if len(i) == 2 and i[0].lower() == "using":
        value = 0
        continue

    if len(i) == 2:
        value += 4
    if j == 1:
        value = 0
        continue

    if len(i) == 3:
        length = contains(i[2])
        if i[1].lower() == "eqv":
            symbols.append([i[0], int(i[2]), length, 'A'])
            base = int(i[2])
        else:
            symbols.append([i[0], value, length, "R"])
            if(length != 4):
              value += length
            else:
              value += 4

bases = []
for i in range(0,16):
  if(i == base):
    bases.append(['Y',000000])
  else:
    bases.append(['N',None])
print("\nBase Table (BT)")
print("Base Availability Indicator Contents")
for j,i in enumerate(bases):
    if(i[1] == 0):
      print(j,"\t",i[0],"\t\t\t\t\t\t",str(i[1]) * 6)
    else:
      print(j,"\t",i[0])
