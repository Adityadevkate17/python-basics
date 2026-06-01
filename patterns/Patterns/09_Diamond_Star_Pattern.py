#     *
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     * 

n = int(input("Enter size: "))

#upper pyramid
for i in range(1, n + 1):
#stars
    for j in range(n - i):
             print(" ", end = "")
#spaces
    for j in range(2 *i -1):
             print("*", end ="")
    print()

#lower pyramid
for i in range(n, 0, -1):
#stars
    for j in range(n - i):
             print(" ", end = "")
#spaces
    for j in range(2 * i -1):
             print("*", end ="")
    print()


