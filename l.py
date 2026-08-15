n = int(input())
students=[]
scores =[]
names=[]
for i in range(n):
    name = input()
    score = int(input())
    students.append([name,score])
    scores.append(score)
    q = sorted(set(scores))[-1]

for i,j in students:
    if j == q:
        names.append(i)

names.sort()
for name in names:
    print(name)


# find pairs whose sum is x

q = [2,7,4,5]
n= int(input())
l= []
for i in range(len(q)):
    for j in range(i+1,len(q)):
        if q[i]+q[j] == n:
            l.extend([q[i],q[j]])


for i in l:
    print(i,end=" ")



