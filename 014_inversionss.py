# The goal in this problem is to count the number of inversions of a given sequence.

import sys

def merge_sort_inv(a,left,right):
    inver=0
    if right<=left: return [[a[left]],inver]
    m=left+(right-left)//2
    [x,p]=merge_sort_inv(a,left,m)
    [y,q]=merge_sort_inv(a,m+1,right)
    inver=inver+p+q
    b=[]
    while x!=[] and y!=[]:
        if x[0]<=y[0]:
           b.append(x[0])
           x.pop(0)
        else:
           b.append(y[0])
           y.pop(0)
           inver=inver+len(x)
    b=b+x+y
    return [b,inver]

if __name__=='__main__':
   input=sys.stdin.read()
   n,*a=list(map(int,input.split()))
   print(merge_sort_inv(a,0,n-1)[1])
