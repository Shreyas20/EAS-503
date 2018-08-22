import random as random
import matplotlib.pyplot as plt
%matplotlib inline 
class Walker:
	def __init__(self,x,y):
		self.x=x
		self.y=y
		pos=(x,y)
		self.path=[pos]
	
	def getDir(self,x,y):
		w=random.randint(1,4)
		if w==1:
			x=x+1 
		elif w==2:
			x=x-1 
		elif w==3:
			y=y-1
		elif w==4:
			y=y+1
		pos=(x,y)
		return pos
			
	def walk(self,pos):
		self.path.append(pos)
		print(self.path)
		return self.path
    
iteration=[]
for i in range(0,5):
    myobj=Walker(0,0)
    x=[]
    y=[]
    a=myobj.getDir(0,0)

    while -4<a[0]<4 and -4<a[1]<4:
        myobj.walk(a)
        x.append(a[0])
        y.append(a[1])
        a=myobj.getDir(a[0],a[1])
        b=myobj.walk(a)
    plt.plot(x,y)
    plt.show()
    print("final Position",a)
    itr=len(b)+1
    iteration.append(itr)
    print("No of iterations",itr)
s=sum(list(iteration))
mean=s/(len(iteration))
print('Mean is:',mean)
