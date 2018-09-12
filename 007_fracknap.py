# The goal of this code problem is to implement an algorithm for the fractional knapsack problem.

import sys

def get_optimal_value(capacity,weights,values):
    value=0
    for k in range(0,n):
        if capacity==0:
           return value
        while 0 in weights:
               j=weights.index(0)
               weights.pop(j)
               values.pop(j)
        q=[vi/wi for vi,wi in zip(values,weights)]
        i=q.index(max(q))
        a=min([weights[i],capacity])
        value=value+a*values[i]/weights[i]
        weights[i]=weights[i]-a
        capacity=capacity-a
    return value

if __name__=="__main__":
   data=list(map(int, sys.stdin.read().split()))
   n,capacity=data[0:2]
   values=data[2:(2*n+2):2]
   weights=data[3:(2*n+2):2]
   opt_value=get_optimal_value(capacity,weights,values)
   print("{:.10f}".format(opt_value))
