lst = [1,2,3,4,5]
def mul(x):
     return x*4
result = map(mul,lst)
res = list(result)
a = str(res)[1:-1]
print(a)
tup1 = ('apple','banna', 'orange')
for i in tup1:
     print(tup1)


def getProduct(n): 
  
    product = 1
  
    while (n != 0): 
        product = product * (n % 10) 
        n = n // 10
  
    return product 
  
# Driver Code 
n = 4513
print(getProduct(n)) 



