# 1
# 01
# 101
# 0101
# 10101

n = int(input("Enter size:")) 

for i in range(n):
    for j in range(i, 0, -1):
        print(j%2,end = " ")
    print()

    