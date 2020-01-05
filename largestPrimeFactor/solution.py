def prime(x):
    for i in range(2,(x//2)):
        if x%i==0:
            return 0
    return x

def lpf(y):
    for j in range(y//2,2,-1):
        if prime(j)==j:
            if y%j==0:
                return j
    return 0

print(lpf(13195))