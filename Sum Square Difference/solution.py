def sum_square_diff (last):
    sum_squares=0
    square_sums=0
    for i in range(1,last+1):
        sum_squares+=i**2
        square_sums+=i
    square_sums=square_sums**2
    return square_sums-sum_squares

print(sum_square_diff(100))