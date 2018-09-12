# Given a set of n segments {[a_0,b_0],[a_1,b_1],...,[a_{n−1},b_{n−1}]} with integer coordinates on a line, find the minimum number m of points such that each segment contains at least one point. That is, find a set of integers X of the minimum size such that for any segment [a_i,b_i] there is a point x∈X such that a_i≤x≤b_i.

import sys
from collections import namedtuple

Segment=namedtuple('Segment','start end')

def optimal_points(segments):
    points=[]
    while segments!=[]:
          y=[s.end for s in segments]
          i=y.index(min(y))
          b=y[i]
          points.append(b)
          segments.pop(i)
          nseg=[s for s in segments]
          for s in nseg:
              if s.start<=b: segments.remove(s)
    return points

if __name__ == '__main__':
   input = sys.stdin.read()
   n,*data=map(int,input.split())
   segments=list(map(lambda x: Segment(x[0],x[1]),zip(data[::2],data[1::2])))
   points=optimal_points(segments)
   print(len(points))
   for p in points: print(p, end=' ')
