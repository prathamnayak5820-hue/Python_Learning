for i in range(5):
    for j in range(1,6):
        print(j,end=" ")
    print()


for i in range(5):
    for j in range(1,6):#1,n+1
        print(1,end=" ")
    print()

#n =5
for i in range(1,6):#n+1
    for j in range(1,6):#1,n+1
        print(i*j,end=" ")
    print()


for i in range(1,6): #1,n+1
    for j in range(1,i+1):
        print(j,end="")
    print()

for i in range(1,6): #1,n+1
    for j in range(1,i+1):
        print(i,end="")
    print()


for i in range(5):
    for j in range(1,5-i+1):
        print(j,end=" ")
    print()

for i in range(5):
    for j in range(5-i,0,-1):
        print(j,end=" ")
    print()


for i in range(5):
    for j in range(5,i,-1):
        print(j,end=" ")
    print()


for i in range(5):
    for j in range(5-i,0,-1):
        print(" ",end="")

    for j in range(1,i+1):
        print("*",end="")
    print()


for i in range(5):
    for j in range(5-i,0,-1):
        print("*",end="")

    for j in range(1,i+1):
        print(" ",end="")
    print()


for i in range(10):
    for j in range(10):
            if i==0 or j==0 or i==9 or j==9:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()