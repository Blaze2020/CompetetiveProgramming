#To find the magic no

def calculate(str1):
    a=list(str1)
    for i in range(len(a)):
        b=ord(a[i])
        print(b)



t=int(input())
for i in range(t):
    n=int(input())
    str1=input()
    if len(str1)==n:
        calculate(str1)
    else:
        print("limit exceeded")
