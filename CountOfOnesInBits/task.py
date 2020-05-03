def countBits(n):
    bin_str = "{0:b}".format(n)
    return bin_str.count('1')
