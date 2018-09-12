# Given two integers a and b, find their least common multiple.

import sys

def gcd(a,b):
    if 0 in [a,b] or a==b:
       return max([a,b])
    else: 
       return gcd(min([a,b]),max([a,b])%min([a,b]))

if __name__=='__main__':
    input=sys.stdin.read()
    a,b=map(int,input.split())
    if a==0 or b==0:
       print(0)
    else:
       print(a*b//gcd(a,b))
