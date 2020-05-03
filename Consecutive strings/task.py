"""
You are given an array strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.

Example:
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"

n being the length of the string array, if n = 0 or k > n or k <= 0 return "".

Note
consecutive strings : follow one after another without an interruption
"""


def longest_consec(strarr, k):
    n = len(strarr)
    if (n == 0) or (k > n) or (k <= 0):
        return ''

    current_max = 0
    current_max_index = 0
    for index in range(0, n - k + 1):
        current_max_value = sum(len(strarr[i]) for i in range(index, index + k))
        if current_max_value > current_max:
            current_max = current_max_value
            current_max_index = index

    return ''.join(strarr[current_max_index:current_max_index+k])


print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))
print(longest_consec(["ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"], 1))

