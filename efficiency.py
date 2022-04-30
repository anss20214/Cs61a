def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 2) + fib(n - 1)


from math import sqrt
def count_factors(n):
    """ total number of times this process executes the body of the while statement is the greatest integer less than sqrt(n)
     w is the number of statements in the while body
     v  is the number of statements outside of the while statement"""

    sqrt_n = sqrt(n)
    k, factors = 1, 0
    while k < sqrt_n:
        if n % k == 0:
            factors += 2
        k += 1
    if k * k == n:
        factors += 1
    return factors

result = count_factors(576)

