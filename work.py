import test

bigp = test.animal(4, "dlrt", None)
alist = []

f = open("data", "r")
for line in f:
    mlist = line.split(',')
    mlist[-1] = mlist[-1].strip()

    tempa = test.animal(int(mlist[0]), mlist[1], mlist[2])
    alist.append(tempa)

for a in alist:
    a.ppar()

print("ENDE! he")
