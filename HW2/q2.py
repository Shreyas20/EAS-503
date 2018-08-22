import re,string,math
from sympy import Symbol, Poly
class Represent:
	def __init__(self,p):
		self.p=p
		a=str.replace(self.p,"-", "+-")
		s=re.split(r'[+]', a)
		print(s)
		
class Polynomial:
	def __init__(self,p):
		self.p=p
	def getCoef(self):
		
		x = Symbol('x')
		self.co=Poly(str(self.p), x).all_coeffs()
		cof = self.co[::-1]
		return cof
	def order(self):
		o=self.getCoef()
		return (len(o)-1)
	def solve(self):
		l=self.getCoef()
		
		if self.order()==2:
			a=float(l[2])
			b=float(l[1])
			c=float(l[0])
			d=b**2-4*a*c
			sol1 = (-b-(d**(0.5)))/(2*a)
			sol2 = (-b+(d**(0.5)))/(2*a)
			sol=[sol1,sol2]
			#print("Solution of the equation",sol)
			return sol
		else:
			return "Entered equation is not quadratic"
		
	def __add__(self,other):
		c1=self.getCoef()
		c2=other.getCoef()
		k=(max(self.order(),other.order()))
		addlist=[0]*(k+1)
		dif=abs(self.order()-other.order())
		for j in range(0,dif+1):
			if len(c1)>len(c2):
				c2.append(0)
			elif len(c2)>len(c1):
				c1.append(0)
		for i in range(0,k+1):
			addlist[i]=c1[i]+c2[i]
		if len(addlist)==1:
    			return addlist[0]
		elif len(addlist)>1:
			addition=[str(addlist[0])]
			for i in range(1,len(addlist)):
				x=str(addlist[i])+'*x**'+str(i)
				addition.append(str(x))
			addition1=addition[::-1]
			s='+'.join((addition1))
			a=str.replace(s,"+-", "-")
			return a
				    
	def __mul__(self,other):
		c1=self.getCoef()
		c2=other.getCoef()
		k1=self.order()
		k2=other.order()
		m=k1+k2+1
		mullist=[0]*(m)
		#print(mullist)
		for i in range(0,k1+1):
			for j in range(0,k2+1):
				l=i+j
				mullist[l]=c1[i]*c2[j]+mullist[l]
		resmul=mullist[::-1]
		return resmul
   #x**2-3*x+5
   #2*x 
	def __sub__(self,other):
		
		c1=self.getCoef()
		c2=other.getCoef()
		k=(max(self.order(),other.order()))
		addlist=[0]*(k+1)
		dif=abs(self.order()-other.order())
		for j in range(0,dif+1):
			if len(c1)>len(c2):
				c2.append(0)
			elif len(c2)>len(c1):
				c1.append(0)
		for i in range(0,k+1):
			addlist[i]=c1[i]-c2[i]
		resadd=addlist[::-1]
		#print("Addition is",resadd)
		return resadd       
	def __del__(self):
		pass


term1=input("\nEnter a polynomial in the string format(a*x**2+b*x+c) on which you want to perform the operations")
t=Represent(term1)
print(type(term1))
Survey=input("\nAre you going to perform mathematical operations?(Y/N)")
if Survey=='Y' or Survey=='y':
	term2=input("\nEnter a polynomial in the string format(a*x**2+b*x+c)")
	term3=input("Enter a polynomial in the string format(a*x**2+b*x+c)")
	
	t1=Polynomial(term1)
	t2=Polynomial(term2)
	t3=Polynomial(term3)
	T1=t1.getCoef()

t4=t1+t2
T4=Polynomial(t4)
print(T4+t3)
a=t1.getCoef()
print(a)
#print(t1+t4)

