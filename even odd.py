def one(n):
    if n==0:
        return True
    else:
        return two(n-1)
def two(n)    :
    if n==0:
        return False
    else:
        return one(n-1) 
num=int(input("enter a 4 digit number:"))
if one(num):
    print(num,"is even")
else:
    print(num,"is odd")    