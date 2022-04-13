def modify_array(n):
    for i in n:
        if 0 in n:
            n.remove(0)
            n.append(0)
    return n
print(modify_array([1,3,0,4,0,2]))       
