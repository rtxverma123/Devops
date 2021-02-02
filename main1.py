x = input('Enter a number: ')

def prod(a):
    num = 1
    while (a!=0): 
        num = num * a
        a = a % 10
        a = a//10
    return num

y = prod(x)
print(y)
    
