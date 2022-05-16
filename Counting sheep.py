# https://www.codewars.com/kata/54edbc7200b811e956000556


def count_sheeps(sheep):
    result = 0
    for i in sheep:
        if i:
            result += 1
    return result


def count_sheeps2(sheep):
    return sheep.count(True)