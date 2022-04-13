from calendar import c
from turtle import st


def repeted_char(str1):
    char_order = []
    counts = {}

    for i in str1:
        if i in counts:
            print(i)
            counts[i] +=1
        else:
            counts[i] = 1
            char_order.append(i)
    
    for i in char_order:
        if counts[i] == 1:
            return i
    return None

print(repeted_char("krishnaa"))