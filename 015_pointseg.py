# In this problem you are given a set of points on a line and a set of segments on a line. The goal is to compute, for each point, the number of segments that contain this point.

import sys

def fast_count_segments(starts,ends,points):
    starts=[[i,-1] for i in starts]
    starts.sort()
    ends=[[i,1] for i in ends]
    ends.sort()
    points=[[i,0,j] for i,j in zip(points,range(0,len(points)))]
    points.sort()
    mega=starts+ends+points
    mega.sort()
    count=0
    values=[]
    for i in mega:
        if i[1]==-1:
           count=count+1
        elif i[1]==0:
           values.append([i[2],count])
        else:
           count-=1
    values.sort()
    return [i[1] for i in values]


if __name__=='__main__':
   input=sys.stdin.read()
   data=list(map(int,input.split()))
   n=data[0]
   m=data[1]
   starts=data[2:2*n+2:2]
   ends=data[3:2*n+2:2]
   points=data[2*n+2:]
   cnt=fast_count_segments(starts,ends,points)
   for x in cnt: print(x,end=' ')
