def smallest_mult (x,y):
    start = y
    divisible = False
    while not divisible:
        i = x
        while start%i==0 and i<y:
            i+=1
            divisible = True
        if start%i!=0:
            start+=y
            divisible = False
    return start

print(smallest_mult(1,20))