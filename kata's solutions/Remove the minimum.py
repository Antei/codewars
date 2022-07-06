# https://www.codewars.com/kata/563cf89eb4747c5fb100001b

from os import remove


def remove_smallest(numbers: list):
    lst = []
    lst = lst + numbers
    if numbers:
        lst.remove(min(numbers))
    return lst

def remove_smallest(numbers: list):
    lst = numbers[:]
    if lst:
        lst.remove(min(lst))
    return lst