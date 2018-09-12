# To force the given implementation of the quick sort algorithm to efficiently process sequences with few unique elements, your goal is replace a 2-way partition with a 3-way partition. That is, your new partition procedure should partition the array into three parts: < x part, = x part, and > x part.

import sys
import random

def partition3(a,l,r):
    x,j,t=a[l],l,l
    for i in range(l+1,r+1):
        if a[i]<x:
           j+=1
           a[i],a[j]=a[j],a[i]
        if a[i] == x:
           j+=1
           a[i],a[j]=a[j],a[i]
           a[j],a[t+1]=a[t+1],a[j]
           t+=1
    h=min(t-l+1,j-t)
    for i in range(h): a[l+i],a[j-i]=a[j-i],a[l+i]
    return [l+j-t,j]


def randomized_quick_sort(a,l,r):
    if l>=r: return
    k=random.randint(l,r)
    a[l],a[k]=a[k],a[l]
    [p,q]=partition3(a,l,r)
    randomized_quick_sort(a,l,p-1)
    randomized_quick_sort(a,q+1,r)


if __name__=='__main__':
   input=sys.stdin.read()
   n,*a=list(map(int,input.split()))
   randomized_quick_sort(a,0,n-1)
   for x in a: print(x,end=' ')
