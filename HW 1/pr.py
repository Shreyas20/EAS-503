import time
l=[]
s=time.time()
def main():
	PrimeTester()
	print('\n**List of first 50 numbers:**\n',l)
	print('\nLength of the list is:',len(l))
	e=time.time()
	print('\nTime required to run the function is:',e-s)
def PrimeTester():
	count=1
	c=0
	while(c<50):
		count=count+1
		for i in range(2,count):
			if count%i==0:
				break				
		else:	
			l.append(count)
			c=c+1
main()
