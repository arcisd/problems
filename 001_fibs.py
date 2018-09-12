# Given an integer n, find the nth Fibonacci number F_n.

def calc_fib_faster(n):
    F=[0,1]
    for i in range(2,n+1): F.append(F[i-1]+F[i-2])
    return F[n]

n=int(input())
print(calc_fib_faster(n))
