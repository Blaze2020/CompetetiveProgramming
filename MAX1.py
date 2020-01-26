# TO find the maximum no of one's

def calculatesetbits(N):
        list2=[]
        buffer=[]
        for i in range(N,0,-1):
            buffer.append(i)
            binary=bin(i).replace("0b","")
            list1=list(binary)
            list2.append(list1.count('1'))

        a=max(list2)
        for j in range(len(list2)):
            if a==list2[j]:
                print(N-j)
                break






t=int(input())

if 1<=t<=1000:
    for i in range(t):
        N=int(input())
        if 1<=N<=pow(10,9):
                calculatesetbits(N)


