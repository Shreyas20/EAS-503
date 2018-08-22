# Using matplotlib for plotting
import matplotlib.pyplot as plt
%matplotlib inline 
import time

t1m=[]

t10m=[]
i10k=10000
for i in range(0,100):
    l1m=list(range(1,1000001)) #recreation of the list
    s=time.time()
    del(l1m[i10k])
    e=time.time()
    x=e-s
    t1m.append(x) #creating list of deletion time
    i10k=+10000

print('\n\n')
print('####Length of the list which contains elements from 1 to 1m after deletion:\n\n',len(l1m))
print('####List of time required for deletion of list having 10m elements:\n\n',t1m)
print('####No of elements deleted:',len(t1m))

j1m=100000
for j in range(0,100):
    l10m=list(range(1,10000001))
    s=time.time()
    del(l10m[j1m])
    e=time.time()
    x=e-s
    t10m.append(x)
    j1m=+100000
print('\n\n')  
print('Length of the list which contains elements from 1 to 10m after deletion:\n\n',len(l10m))
print('List of time required for deletion of list having 10m elements:\n\n',t10m)
print('No of elements deleted:\n\n',len(t10m))
print('Comparison of deletion time for various values of indices are plotted on the graph where position of element is plotted on x-axis and time required for deletion on y-axis')
print('Graph contains plot for two different lists which shows time of deletion depends on the size of the list')
x=list(range(0,100))
plt.plot(x,t1m)
plt.title('Deletion from the list with 1M elements')
plt.show()
plt.plot(x,t10m)
plt.title('Deletion from the list with 10M elements')
plt.show()
plt.plot(x,t1m)
plt.plot(x,t10m)
plt.title('Comparison of deletion time from two different lists')
plt.show()
