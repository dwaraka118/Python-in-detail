# write a program to print multiplication table according to user input

n = int(input("enter the number for which you want multiplication table : "))
for i in range(1,11):
    mul = n * i
    print(f'\n{n} * {i} = {mul}')

# Expected output
    '''enter the number for which you want multiplication table : 7
    7 * 1 = 7
    7 * 2 = 14
    7 * 3 = 21
    7 * 4 = 28
    7 * 5 = 35
    7 * 6 = 42
    7 * 7 = 49
    7 * 8 = 56
    7 * 9 = 63
    7 * 10 = 70'''
