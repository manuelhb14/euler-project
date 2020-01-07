def prime(num):
    for i in range(2,int(num**(1/2))+1):
        if num%i==0:
            return False
    return True

prime_count = 0
x = 1
while prime_count!=10001:
  x+=1
  if prime(x)==True:
      prime_count+=1

print(x)