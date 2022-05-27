# https://www.codewars.com/kata/576757b1df89ecf5bd00073b/

def tower_builder(n_floors):
    return [str('*' * (i + i - 1)).center(n_floors * 2 - 1) for i in range(1, n_floors + 1)]



print(tower_builder(1))
print(tower_builder(2))
print(tower_builder(3))