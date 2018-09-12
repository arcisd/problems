# The goal in this problem is to find the minimum number of coins needed to change the input value (an integer) into coins with denominations 1, 5, and 10.

import sys

def get_change(n):
    C=[]
    if n==0:
       return 0
    else:
         while n-10>=0:
               C.append(10)
               n=n-10
         while n-5>=0:
               C.append(5)
               n=n-5
         while n-1>=0:
               C.append(1)
               n=n-1
    return len(C)
          

if __name__=='__main__':
   n=int(sys.stdin.read())
   print(get_change(n))
