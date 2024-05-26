print("Lower triangular Pattern:")
for i in range(1,6):
    for j in range(0,i):
        print("*",end="")
    print()

print("Upper triangular Pattern:")  
for i in range(6,1,-1):
    for j in range(0,i):
        print("*",end="")
    print()

print("Pyramid Pattern:")  
for i in range(5):
        print(' ' * (5 - i - 1) + '*' * (2 * i + 1))