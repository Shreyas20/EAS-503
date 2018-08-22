
class Polynomial:
    def __init__(self, dictionary):
        self.d = dictionary


    def __call__(self, x):
        s = 0

        for key in d.keys:
            s += self.d[key]*x**key
        return s

   


p = Polynomial({1:1,100:-3})
p2 = Polynomial({1:-1,20:1,100:4})

print(p) 
print(p2)
#print(p+p2)
