n = float(input('enter the number for which you wanted to check : '))
if n > 0 :
    print(n,"is a postive number")
elif n < 0:
    print(n ,"is a negative number")
else:
    print(n,"number is zero")

pn = [print(f'{n} is + number') if n > 0 else print(f'{n} is - number')]