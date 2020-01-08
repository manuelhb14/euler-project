def py_triplet ():
    for i in range(1,999):
        for j in range(1,999):
            for k in range(1,999):
                if (i+j+k)==1000 and (i**2+j**2)==(k**2):
                    return (i,j,k, i*j*k)

print(py_triplet())