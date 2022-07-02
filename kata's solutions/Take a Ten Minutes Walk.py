# https://www.codewars.com/kata/54da539698b8a2ad76000228

def is_valid_walk(walk):
    x, y, timer = 0, 0, 10

    for step in walk:
        if step == 'n':
            y += 1
        if step == 's':
            y -= 1
        if step == 'w':
            x -= 1
        if step == 'e':
            x += 1
        timer -= 1
    return (x, y) == (0, 0) and timer == 0


#some test cases for you...
print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']), 'should return True')
print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']), 'should return False')
print(is_valid_walk(['w']), 'should return False')
print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s']), 'should return False')


# def isValidWalk(walk):
#    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')