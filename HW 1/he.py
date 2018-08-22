def main():
	computeMean()

def computeMean():
	l=[]
	#s=0
	#count=0
	with open('data_p2.txt','r') as f: 
		for line in f: 
			s = line.strip() 
			try:
				c=float(s)
				l.append(c)
			except ValueError:
				pass
				#c=0
	s=sum(list(l))
	mean=s/(len(l))
	print('Mean is:',mean)	
			
main()	      
