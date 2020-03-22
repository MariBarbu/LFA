def bkt (x, litera, k):
    global l, cuvant, p
    if k == len (cuvant):
        if x in p :
            return True
    else:
        for j in range (len (l)):
            if l[x][j] != 0 and litera in l[x][j]:
                litera = cuvant[k]
                k += 1
                if bkt(j, litera, k):
                    return True
def accept(st,n):
    global l, cuvant, st_init
    if bkt(st, cuvant[n] ,n):
        return True
    else:
        for i in range(len(l)):
            if l[st][i]!=0 and cuvant[n] in l[st][i]:
                if bkt(i, cuvant[n+1], n+1):
                    return True

f=open("fisier", "r")
cuvant=f.readline() #citim cuvantul de pe prima linie
nr_stari=f.readline() #numarul total de stari
st_init=int(f.readline()) #starea initiala
nr_fin=int(f.readline()) #numarul de stari finale
p=[int(x) for x in f.readline().split()] #starile finale
nr_tranz=int(f.readline())      #numarul de tranzitii
l=[[0 for j in range(int(nr_stari))] for i in range(int(nr_stari))]
tranz=[x.split() for x in f.readlines()]        #tranzitiile, cate una pe o linie de forma "1 2 a" sau "1 2 ab"
for i in tranz:
    l[int(i[0])][int(i[1])]=i[2]
n=0
cuvant=cuvant.replace("#","")
if cuvant == '\n' and st_init in p:
    print("accepted")
elif accept(st_init,0):
    print("acceptat")
else:
    print("neacceptat")
