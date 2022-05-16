# https://www.codewars.com/kata/54c27a33fb7da0db0100040e/

def is_square(n):
    if n >= 0:
        return (n ** 0.5).is_integer()
    else:
        return False