# Creating Calculator app

choice = input(("Enter your choice (add or + / sub or - / mul or *): "))
num1 = int(input('enter the first number : '))
num2 = int(input('enter the second number : '))

if choice == 'add' or choice == '+':
    sum = num1 + num2
    print('adding of two given numbers is : ',sum)
elif choice == 'sub' or choice == '-':
    sub = num1 - num2
    print('substraction of two numbers is : ',sub)
elif choice == 'mul' or choice == '*':
    mul = num1 * num2
    print('product of two numbers is : ',mul)
else:
    print('please choose from above options ')

# assignment : add division option