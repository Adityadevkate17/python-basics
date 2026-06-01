# A
# AB
# ABC
# ABCD
# ABCDE


n = int(input("Enter size:")) 

for i in range(1, n + 1):
    ch = 'A'

    for j in range(i):
        print(ch, end="")
        ch = chr(ord(ch) + 1) ## Move to next alphabet (A→B, B→C, ...)

    print()

