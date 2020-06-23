# what is a function ?

'''f(x) = x ^ 2 + 5 
f(1) = 6
f(2) = 9'''

def greet(name):
    print(f"hey! {name} i am always there for you")
    return f"\n hey! {name} i am always there for you "

g = greet('Dwaraka')
g1 = greet('kishore')
print(g,g1)


def add(num1,num2):
    sum = num1 + num2
    # print(f"sum of two given numbers {num1},{num2} is : {sum}")
    return sum
a = add(1,2)
b =add(num2=5,num1=3)
print(a,b)

def sub(n1,n2):
    substract = n1 - n2
    print(substract)
sub(5,4)



def mean1(a,b):
    m = (a+b)/2
    print(m)
mean1(2,4)