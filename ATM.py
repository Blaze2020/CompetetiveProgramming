#CODE CHEF-ATM
tax=0.50
x,y=map(float,input().split())
if (0<x<=2000) and (0<=y<=2000) and (x%5==0) and  (x<=y):
    newbalance=y-(x+tax)
    print( "%.2f"%round(newbalance,2))
else:
    print("%.2f"%round(y,2))


