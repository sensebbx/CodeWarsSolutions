"""
Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

 "(p1**n1)(p2**n2)...(pk**nk)"
with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
"""


def primeFactors(n):
    i = 2
    factors = {}
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            if i in factors.keys():
                factors[i] += 1
            else:
                factors[i] = 1
    if n > 1:
        factors[n] = 1
    return '('+')('.join(str(key)+('**' + str(value) if value > 1 else '') for key, value in factors.items() if value > 0) + ')'
