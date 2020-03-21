import sys as s
# Write your code here
"""import math
def countDivisors(n):
        cnt = 0
        for i in range(1, (int)(math.sqrt(n)) + 1):
            if (n % i == 0):

                # If divisors are equal,
                # count only one
                if (n / i == i):
                    cnt = cnt + 1
                else:  # Otherwise count both
                    cnt = cnt + 2

        print(cnt)




def query(l ,r ,list1):
    prod=1
    for i in range(list1.index(l),(list1.index(r)+1)):
        if 1<= list1[i] <= 10:
            prod*=list1[i]
    countDivisors(prod%(pow(10,9)+7))




N, M = map(int, input().split())
if 1 <= N <= (5 * pow(10, 5)) and 1 <= N <= (4 * pow(10, 5)):
    list1 = list(map(int, input().split()))
    for i in range(M):
        l, r = map(int, input().split())
        if 1 <= l <= r <= N:
            query(l, r, list1)"""
"""def calculate(list1, n, k):
    list1.sort()
    if list1[0]>=k:
        print(0)
    else:
        print(k-list1[i])"""


#t=int(input())
"""if 1<=t<=5:
    for i in range(t):
        n,k=map(int,input().split())
        if 1<=n<=pow(10,5):
            list1=list(map(int,input().split()))
            calculate(list1,n,k)"""

'''File CLassifier'''
extension=['exe','pdf','docx','pptx','mdj','json']
def classifybasedonextension(directory):
    print('FILE TYPE', '\t', 'FILE NAME', '\t', 'FILE SIZE')
    for i in range(len(directory)):
        for j in range(len(extension)):
            if directory[i].split('.')[1]==extension[j]:
                print(directory[i].split('.')[1],'\t\t',directory[i].split('.')[0],'\t\t\t',s.getsizeof(directory[i]))



n=int(input())
directory=[]
for i in range(n):
    directory.append(input())

classifybasedonextension(directory)









