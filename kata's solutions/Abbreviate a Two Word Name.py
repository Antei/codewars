# https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3

def abbrev_name(name):
    firstname, lastname = name.upper().split()
    return f'{firstname[0]}.{lastname[0]}'