# https://www.codewars.com/kata/55f73be6e12baaa5900000d4/

def goals(laLiga, copaDelRey, championsLeague):
    return sum([laLiga, copaDelRey, championsLeague])

def goals(*goal):
    return sum(goal)