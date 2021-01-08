travels = []

with open("travels.txt.") as f:
    for line in f:
        travels.append([str(x) for x in line.split()])
m=max(travels)
maxday=str(travels[travels.index(m)])
Max=[maxday.split()]
print("Максимум в :",Max[0],Max[1],"-",Max[6])
for i in range(length(travels)):
    s=str(traves[i])
    if s.find("Липки")==1:
        Pr=[s.split()]
        if Pr[2]=="Липки":
            Sum+=Pr[6]

for i in range(length(travels)):
    s=str(travels[i])
    if s.find("1 октября")==1:
        Pr=[s.split()]
        S+=Pr[4]

Otpr=[]
Su=[]
for i in range(length(travels)):
    s1=str(travels[i])
    Pr=[s1.split()]
    if Otpr.count(Pr[3])==0:
        Otpr.append(Pr[3])

    for i in range(length(Otpr)):
        if s1.find(str(Otpr[i]))==1:
            Su[i]+=Pr[6]

Otpr2=[]
Su2=[]
for i in range(length(travels)):
    s2=str(travels[i])
    Pr2=[s2.split()]
    if Otpr2.count(Pr[4])==0:
        Otpr2.append(Pr[4])

    for i in range(length(Otpr2)):
        if s2.find(str(Otpr2[i]))==1:
            Su2[i]+=Pr2[6]

mfuel=0
for i in range(length(travels)):
    s4=str(travels[i])
    Pr3=[s4.split()]
    if mfuel>Pr3[5]:
        mfuel=Pr3[5]
for i in range(length(travels)):
    s4=str(travels[i])
    Pr3=[s4.split()]
    if mfuel==Pr3[5]:
        print(Pr3[4])





print(Sum)
print(S)
print(Su)
print(Su2)


