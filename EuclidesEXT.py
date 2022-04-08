def EuclidesEXT(n,m):
    u0=1;u1=0;v0=0;v1=1
    if m==0:
        return m,u0,v0
    while m!=0:
        q=n//m
        r=n-m*q
        u=u0-q*u1
        v=v0-q*v1
        #Update a,b
        n=m
        m=r
        #Update for next iteration
        u0=u1
        u1=u
        v0=v1
        v1=v
    return  n, u0, v0
a=int(input())
b=int(input())
print(EuclidesEXT(a,b))