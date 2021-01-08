Perepis = []

with open("Perepis.txt") as f:
    for line in f:
        Perepis.append([str(x) for x in line.split()])
minim=1958
k=0
rang=int(input())
for i in range(length(Prerepis)):
    if Perepis.count(minim)!=0 and minim<1978:
        k+=Perepis.count(minim)
        minim+=1
    k1=Perepis.count(rang)

    print(k,k1)