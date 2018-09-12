# Given two integers a and b, find their greatest common divisor.

def gcd(a,b):
    if 0 in [a,b] or a==b:
       return max([a,b])
    else: 
       return gcd(min([a,b]),max([a,b])%min([a,b]))

print(gcd(int(input()),int(input())))    
