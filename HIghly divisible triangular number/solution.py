def triangle_numbers(n):
    x = 0
    for i in range(n+1):
        x+=i
    return x

def divisors(x):
    div = 1
    for i in range(1,x//2+1):
        if x%i==0:
            div+=1
    return div

x = 1
y = triangle_numbers(x)
p = divisors(y)

while p < 500:
    x+=1
    y = triangle_numbers(x)
    p = divisors(y)

print(y, p)