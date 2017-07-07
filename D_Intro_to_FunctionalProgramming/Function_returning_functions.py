# program to calculate polynomials
def polynomial_creator(*coefficients):  # variable arguements
    """ coefficients are in the form a_0, a_1, ... a_n 
    """
    def polynomial(x):
        res = 0
        for index, coeff in enumerate(coefficients):
            res += coeff * x** index
        return res
    return polynomial
  
p1 = polynomial_creator(4)       #4 
p2 = polynomial_creator(2, 4)    # 4x +2
p3 = polynomial_creator(2, 3, -1, 8, 1)  # x**4+8x**3-1x**2+3x+2  
p4  = polynomial_creator(-1, 2, 1) # similar


for x in range(-2, 2, 1):
    print(x, p1(x), p2(x), p3(x), p4(x))

"""
Output:
(-2, 4, -6, -56, -1)
(-1, 4, -2, -9, -2)
(0, 4, 2, 2, -1)
(1, 4, 6, 13, 2)
"""
