'''permutations of char in a tree recursion'''
def permute(s,bucket=' '):
    if not s:
        print(bucket)
        return
    for i in range(len(s)):
        permute(s[:i] + s[i+1:], bucket + s[i])



text=input("Enter a name /word")
print("possibilities of combinations are:")
permute(text)
