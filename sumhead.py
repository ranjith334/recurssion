def sumhead(n):
    if n == 0:
        return 0
    else:
        return n + sumhead(n - 1)


num=int(input("enter a number"))
print("sum:",sumhead(num))
def sumtail(n,temp=0):
    if n==0:
        return temp
    return sumtail(n-1, temp + n)
num=int(input("enter a number"))
print("sum:",sumtail(num))
