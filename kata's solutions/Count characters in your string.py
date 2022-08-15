# https://www.codewars.com/kata/52efefcbcdf57161d4000091/

def count(string: str):
    return dict((c, string.count(c)) for c in set(string))