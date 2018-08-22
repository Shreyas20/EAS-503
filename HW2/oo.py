from operator import add

class Poly:

     def __init__(self,coeffs):
         self.degree = len(coeffs)-1
         self.rep = self.__str(coeffs)
         coeffs.reverse()
         self.coeffs = coeffs

     def __str(self,coeffs):
        terms = [" + ("+str(coeffs[k])+"*x**" + \
                 str(self.degree-k)+")" \
                 for k in range(len(coeffs)) \
                 if coeffs[k]!=0]
        return reduce(add,terms)

     def __repr__(self):
         return self.rep

     def __call__(self,val):
         sum = 0
         return reduce(add,[self.coeffs[i]*val**i \
                            for i in range(len(self.coeffs))])

     def __add__(self,other):
         """Adds two polynomials together, assuming the coeffs are
            ordered by ascending degree."""
         sum_terms = [0] * max(len(self.coeffs),
                               len(other.coeffs))
         for i in range(len(self.coeffs)):
             sum_terms[i] = self.coeffs[i]
         for i in range(len(other.coeffs)):
             sum_terms[i] = sum_terms[i] + other.coeffs[i]
         sum_terms.reverse()
         return Poly(sum_terms)
p = poly.__str([1,2,3])
q = poly.__str([3,1,2,3])
print(p)
print(q)
print(p+q)
