def EuclidesEXT(n,m):
    x0=1;x1=0;y0=0;y1=1
    if m==0:
        return m,x0,y0
    while m!=0:
        q=n//m
        r=n-m*q
        x=x0-q*x1
        y=y0-q*y1
        n=m
        m=r
        x0=x1
        x1=x
        y0=y1
        y1=y
    return  n, x0, y0
a=int(input())
b=int(input())
print(EuclidesEXT(a,b))
