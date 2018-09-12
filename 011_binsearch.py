# The goal in this code problem is to implement the binary search algorithm.

import sys

def binary_search(a,x,low,high):
    if high<low:
       return -1
    mid=low+int((high-low)/2)
    if a[mid]==x:
       return mid
    elif x<a[mid]:
         return binary_search(a,x,low,mid-1)
    else:
         return binary_search(a,x,mid+1,high)

def linear_search(a,x):
    for i in range(len(a)):
        if a[i]==x: return i
    return -1

if __name__=='__main__':
   input=sys.stdin.read()
   data=list(map(int,input.split()))
   n=data[0]
   m=data[n+1]
   a=data[1:n+1]
   for x in data[n+2:]: print(binary_search(a,x,0,len(a)-1),end=' ')
