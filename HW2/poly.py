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
		self.co=Poly(self.p, x).all_coeffs()
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
		print(c1)
		print(c2)
		for i in range(0,k+1):
			addlist[i]=c1[i]+c2[i]
		resadd=addlist[::-1]
		#print("Addition is",resadd)
		return resadd
    
	#def __mul__(self,p,p1):
	#	for i in range(
        


term1=input("Enter a polynomial in the string format(a*x**2+b*x+c) on which you want to perform the operations")
t=Represent(term1)
Survey=input("Are you going to perform mathematical operations?(Y/N)")
if Survey=='Y' or Survey=='y':
	term2=input("Enter a polynomial in the string format(a*x**2+b*x+c)")
	#term3=input("Enter a polynomial in the string format(a*x**2+b*x+c)")
	
	t1=Polynomial(term1)
	t2=Polynomial(term2)
	print('Coefficients of addition of polynomial is:',t1+t2)
else:
	t1=Polynomial(term1)
z=t1.getCoef()
print("Coef are:",z)
order1=t1.order()
print("order is",order1)
eq1=t1.solve()
print('solution of',term1,'is',eq1)
eq2=t2.solve()
print('solution of',term2,'is',eq2)
