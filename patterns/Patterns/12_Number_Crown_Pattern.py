# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321 

n = int(input("Enter size:")) 

for i in range(1,n+1):
#left side

    for j in range(1,i+1):
        print(j, end="")

#spaces
    for j in range(2 * (n-i)):
        print(" ", end ="")

#Right side
    for j in range(i, 0, -1):
        print(j, end="")

    print()    



