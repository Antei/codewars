# https://www.codewars.com/kata/52fba66badcd10859f00097e


#def disemvowel(string_: str):
#    vowels = ['a', 'e', 'i', 'o', 'u']
#    string_ = ''.join(i for i in string_ if i.lower() not in vowels)
#    return string_


def disemvowel(string_: str):
    return ''.join(i for i in string_ if i.lower() not in 'aeiou')