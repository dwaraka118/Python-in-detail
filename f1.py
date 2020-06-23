choice = input("enter you choice : ")
num1 = int(input('enter the first number : '))
num2 = int(input('enter the second number : '))


def add(num1,num2):
    sum = num1 + num2
    print(num1,"+",num2,"=",sum)
def sub(num1,num2):
    sub = num1 - num2
    print(num1,"-",num2,"=",sub)
def mul(num1,num2):
    mul = num1 * num2
    print(f"{num1} * {num2} = {mul}")
def div(num1,num2):
    div = num1 / num2
    print(f'{num1} / {num2} = {div}')


if choice == 'add':
    add(num1,num2)
elif choice == 'sub':
    sub(num1,num2)
elif choice == 'mul':
    mul(num1,num2)
elif choice == 'div':
    div(num1,num2)
else:
    print("you made a wrong choice")