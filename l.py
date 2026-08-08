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


