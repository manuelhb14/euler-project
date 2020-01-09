def palindrome():
    x = 0
    for i in range(1000,900,-1):
        for j in range(1000,900,-1):
            y = i*j
            y = str(y)
            if int(y) > x and len(y)%2==0 and y==y[::-1]:
                x = int(y)
                p = (i,j)
    return x, p

print(palindrome())