"""
Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

 "(p1**n1)(p2**n2)...(pk**nk)"
with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
"""
# import math


# def primeFactors(n):
#     prime = [True for i in range(n + 1)]
#     p = 2
#     while p * p <= n:
#         if prime[p]:
#             for i in range(p * 2, n + 1, p):
#                 prime[i] = False
#         p += 1
#     prime[0] = False
#     prime[1] = False
#     primes = [x for x in range(n + 1) if prime[x]]
#
#     decompression = {key: 0 for key in primes}
#
#     for key, value in decompression.items():
#         while n % key == 0:
#             n = n / key
#             decompression[key] += 1
#
#     return '('+')('.join(str(key)+('**' + str(value) if value > 1 else '') for key, value in decompression.items() if value > 0) + ')'

def primeFactors(n):
    i = 2
    factors = {key: 0 for key in range(n)}
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors[i] += 1
    if n > 1:
        factors[n] = 1
    return '('+')('.join(str(key)+('**' + str(value) if value > 1 else '') for key, value in factors.items() if value > 0) + ')'


print(primeFactors(7775460))
