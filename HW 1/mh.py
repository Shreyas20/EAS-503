import random as random
import time as time
def main():
	s=time.time()
	simulategame()
	e=time.time()
	print('Time required to run the monty hall problem',e-s)
def simulategame():
	door=list(range(0,3))
	win=0	
	stick=0
	switch=0
	while(win<1000):
		car=random.choice(door)
		carlist=[car]
		pick=random.choice(door)
		pickList=[pick]
		montyChoice=[x for x in door if x not in pickList+carlist]
		m=random.choice(montyChoice)
		montrySelect=[m]
		sw=[u for u in door if u not in montrySelect+pickList]
		repick=[pick,sw[0]]
		r=random.choice(repick)
		if r==pick and r==car:
			win+=1
			stick+=1
		elif r==sw[0] and r==car:
			win+=1
			switch+=1
	print('win by sticking:',(stick/win)*100,'%')
	print('win by switching:',switch/win*100,'%')

	print(stick)
	print(switch)
	print(win)
main()

