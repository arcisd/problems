# 010. The goal of this problem is to represent a given positive integer n as a sum of as many pairwise distinct positive integers as possible. That is, to find the maximum k such that n can be written as a_1+a_2+···+a_k where a_1,...,a_k are positive integers and a_i\neq a_j for all 1≤i<j≤k.

import sys

def optimal_summands(n):
    k=n
    l=1
    summands=[]
    while k!=0:
          if k<=2*l:
             summands.append(k)
             k=0
          else:
             summands.append(l)
             k=k-l
             l=l+1
    return summands

if __name__=='__main__':
   input=sys.stdin.read()
   n=int(input)
   summands=optimal_summands(n)
   print(len(summands))
   for x in summands: print(x,end=' ')
