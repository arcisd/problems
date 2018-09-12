# Given an integer n, find the last digit of the nth Fibonacci number F_n (that is, F_n mod 10).

def calc_fib_last(n):
    F=[0,1]
    for i in range(2,n+1): F.append((F[i-1]+F[i-2])%10)
    return F[n]

print(calc_fib_last(int(input())))
