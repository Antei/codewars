# https://www.codewars.com/kata/5715eaedb436cf5606000381/

def positive_sum(arr: list):
    lst = [i for i in arr if i > 0]
    if lst:
        return sum(lst)
    return 0


def positive_sum(arr: list):
    return sum(i for i in arr if i > 0)