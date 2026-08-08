l = [2 ,2 ,2,11 ,14 ,20 ,20]

maxi = l[0]

for i in l:
    if maxi > i:
        maxi = i

slargest = float('-inf')

for i in l:
    if i > maxi and i < slargest:
        slargest = i

print(maxi, slargest)

ferq={}
odd =0
even =0
for i in l:
    if i%2==0:
        even+=1
    else:
        odd+=1
print(odd,even)

for i in l:
    ferq[i]=ferq.get(i,0)+1
print(ferq)


nothing=[]
for i in l:
    if i not in nothing:
        nothing.append(i)
print(nothing)
r_list=[]
w =len(l)-1
for i in range(len(l)):
    r_list.append(l[w-i])
print(r_list)
    




