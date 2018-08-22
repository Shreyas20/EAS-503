import time
primeNos=[]
t=time.time()
def Main():
    primeTester()
    t1=time.time()
    print(t1-t)
    print('nos',primeNos)
    
def primeTester():
    count = 0
    x=1
    while count <50:
        x+=1
        for i in range (2,x-1):
            if x%i==0:
                break
        else:
            primeNos.append(x)
            count+=1     
Main()
