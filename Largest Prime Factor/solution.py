def prime(num):
    for i in range(2,int(num**(1/2))):
        if num%i==0:
            return False
    return True

def fermat(num):
    for y in range(1,num//2):
        x = (num + y**2)**(1/2)
        if x.is_integer():
            if prime(x-y):
                return (x-y)
    return False

print(fermat(600851475143))