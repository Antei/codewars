# https://www.codewars.com/kata/554ca54ffa7d91b236000023

def delete_nth(order: list, max_e: int):
    result = []
    for i in order:
        if result.count(i) < max_e:
            result.append(i)

    return result