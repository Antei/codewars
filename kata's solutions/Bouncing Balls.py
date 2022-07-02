# https://www.codewars.com/kata/5544c7a5cb454edb3c000047/

def bouncing_ball(h, bounce, window):
    if h > 0 and 0 < bounce < 1 and h > window:
        count = 0
        while h > window:
            count += 1
            h *= bounce
            if h > window:
                count += 1
        return count 
    return -1