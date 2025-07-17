def fib (n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)


num=int(input("enyter terms"))
for i in range (num+1):
    print(fib(i), end=' ')
