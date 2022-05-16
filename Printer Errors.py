# https://www.codewars.com/kata/56541980fa08ab47a0000040/

def printer_error(s):
    count = 0
    alph = str([chr(97 + i) for i in range(13)])
    for char in s:
        if char not in alph:
            count += 1
    return f'{count}/{len(s)}'

from re import sub

def printer_error2(s):
    return f'{len(sub("[a-m]", "", s))}/{len(s)}'