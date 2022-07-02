# https://www.codewars.com/kata/5390bac347d09b7da40006f6

def to_jaden_case(string):
    sent_lst = [i.capitalize() for i in string.split()]
    return ' '.join(sent_lst)


def to_jaden_case2(string):
    return " ".join(w.capitalize() for w in string.split())