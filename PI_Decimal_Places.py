# Python fun:  Digits of π
def pi(places):
  '''
  A function named pi that takes the parameter places which is the number of decimal places of the pi constant.
  This function is based on the Sir Isaac Newton's principle of the decimal places in the constant PI.
  -----------------------
  The Variables Defintions
  -----------------------
  c: cumulative sum (increasingly better approximation)
  t: one term in the sum
  n: numerator
  d: denominator
  na: adjustment to numerator for each term
  da: adjustment to denominator for each term
  one: express 1.0 as a long integer with a given number of places

  Returns:
          The decimal numbers of PI depending on the number of places you put in the function.
  @author: Sodiq Agunbiade
  Created on 17-04-2020
  '''
    extra = 8
    one = 10 ** (places+extra)
    t, c, n, na, d, da = 3*one, 3*one, 1, 0, 0, 24
    while t > 1:
        n, na, d, da  = n+na, na+8, d+da, da+32
        t = t * n // d
        c += t
    return c // (10 ** extra)

print(pi(10000))