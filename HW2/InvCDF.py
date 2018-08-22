import numpy as np
import math
import matplotlib.pyplot as plt
%matplotlib inline 
s=(np.random.uniform(low=0.0, high=1.0, size=100)).tolist()
dist=[]
for i in range(0,100):
    x=(math.log(1-s[i]))/-4
    dist.append(x)    
s=sum(list(dist))
mean=s/len(dist)
print('Mean:',mean)
print('Variance:',np.var(dist))
plt.hist(dist)
plt.title("Exponential Distribution for lambda=4")
plt.xlabel("Value")
plt.ylabel("Frequency")
