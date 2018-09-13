# 017. In this problem, you are given a set of bars of gold and your goal is to take as much gold as possible into your bag. There is just one copy of each bar and for each bar you can either take it or not (hence you cannot take a fraction of a bar).

import sys

def optimal_weight(W,weights):
    n=len(weights)
    weights=[0]+weights
    valueslists=[[0]*(W+1)]
    for i in range(1,n+1):
        wi_list=[0]
        for w in range(1,W+1):
            value_iw=valueslists[i-1][w]
            if weights[i]<=w:
               val=valueslists[i-1][w-weights[i]]+weights[i]
               if value_iw<val: value_iw=val
            wi_list.append(value_iw)
        valueslists.append(wi_list)
    return valueslists[n][W]

if __name__=='__main__':
   input=sys.stdin.read()
   W,n,*w=list(map(int,input.split()))
   print(optimal_weight(W,w))
