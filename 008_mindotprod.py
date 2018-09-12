# The goal is, given two sequences a_1,a_2,...,a_n and b_1,b_2,...,b_n, find a permutation π of the second sequence such that the dot product of a_1,a_2,...,a_n and b_{π_1},b_{π_2},...,b_{π_n} is minimum.

import sys

def min_dot_product(a,b):
    a.sort()
    b.sort()
    b.reverse()
    c=[ai*bi for ai,bi in zip(a,b)]
    return sum(c)

if __name__=='__main__':
   input=sys.stdin.read()
   data=list(map(int,input.split()))
   n=data[0]
   a=data[1:(n+1)]
   b=data[(n+1):]
   print(min_dot_product(a,b))
    
