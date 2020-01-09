def prime(num):
    for i in range(2,int(num**(1/2))+1):
        if num%i==0:
            return False
    return True

x = 2
prime_sum = 0
while x < 2000000:
    if prime(x):
        prime_sum+=x
    x+=1

print(prime_sum)