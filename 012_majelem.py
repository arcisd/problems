# The goal in this code problem is to check whether an input sequence contains a majority element.

import sys

#Boyer–Moore majority vote algorithm.
def get_majority_element(a):
    k=0
    for i in a:
        if k==0:
           element,k=i,1
        elif i==element:
             k+=1
        else:
             k-=1
    k=0
    for i in range(0,len(a)):
        if a[i]==element: k+=1
    if k>n/2:
       return element
    else:
       return -1

if __name__=='__main__':
   input=sys.stdin.read()
   n,*a=list(map(int,input.split()))
   if get_majority_element(a)!=-1:
       print(1)
   else:
       print(0)
