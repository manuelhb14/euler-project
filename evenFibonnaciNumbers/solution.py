def fibbonaci(x,y,suma):
    if y>4000000:
        return suma
    else:
        if (x+y)%2==0:
            suma+=(x+y)
        return fibbonaci(y,x+y,suma)

print(fibbonaci(1,1,0))