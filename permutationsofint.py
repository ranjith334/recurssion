def binary(n,b=''):
    if n==0:
        print(b)
        return
    binary(n-1,b+'0')
    binary(n-1,b+'1')


length=int(input("enter the length of the string: "))
print("binary combinations ....")
binary(length)