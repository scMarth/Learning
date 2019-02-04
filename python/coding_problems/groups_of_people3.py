from itertools import combinations,permutations,repeat,groupby,zip_longest
Peop = [["A001_B","A001_B"],["A004_A","A004_A"],["A003_A","A003_A","A003_A","A003_A","A003_A","A003_A"],["A002_A","A002_A","A002_A","A002_A"],["A001_C","A001_C"],["A001_A","A001_A","A001_A"],["A002_B","A002_B"]];
RPla = [4,10,2,4,8]
Comb = []
for r in RPla:
    out,out1,l1,s1 = [],[],[],[]
    for s in Peop:
        l = len(s)
        if l > r:
            continue
        elif l == r:
            out.append(s)
        else:
            s1.append(s) # ======== new purged Peop
            l1.append(l) # ======== len same people Peop
    indL,tempC,diff = [],[],[]
    for z in range(2,len(l1)-1):
        for k,y in zip(combinations(range(len(l1)),z),combinations(l1,z)):
            indL.append(k)
            tempC.append(y)
            if sum(y) > r:
                continue # <<<<<==== WILL DO SOMETHING ======================
            elif sum(y) == r:
                tempL1 = []
                for h in k:
                    tempL1.append(s1[h])
                tempL1 = [item for sublist in tempL1 for item in sublist] #flatten
                out.append(tempL1)
            else:
                diff = r - sum(y)
                tempL1 = []
                for h in k:
                    tempL1.append(s1[h])
                tempL1 = [item for sublist in tempL1 for item in sublist] #flatten
                tempL1.extend(repeat("Empty Desk",diff))
                out.append(tempL1)