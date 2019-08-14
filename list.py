def count(list1,l,r): 
    c = 0
    for x in list1: 
        if x>= l and x<= r: 
            c+= 1
            return c
list1 = [10, 20, 30, 40, 50, 40, 40, 60, 70] 
l=40
r=80 
printcount(list1, l, r) 
