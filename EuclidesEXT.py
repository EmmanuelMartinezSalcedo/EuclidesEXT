def EuclidesEXT(n,m):
    if m==0:
        return (n,1,0)
    else:
        (d,x2,y2)=EuclidesEXT(m, n%m)
        (x,y)=(y2,x2-(((n/m)-((n/m)%1))*y2))
        return(d,x,y)

def Diofantica(n,m,o,p):
    (d,x0,y0)=EuclidesEXT(n,m)
    d2=o/d
    for i in range(0,p,1):
        x1=(x0*d2)-(m/d)*i
        y1=(y0*d2)-(n/d)*i
        print("x1=",x1,",","y1=",y1)
print("Ingrese a,b")
a=int(input())
b=int(input())
print("(MCD, X, Y)")
print(EuclidesEXT(a,b))
print("¿Desea encontrar la solución a una ecuacion diofantica?(y/n)")
op=str(input())
if op=='y':
    print("Ingrese el resultado de la ecuacion diofantica")
    c=int(input())
    print("¿Cuantos posibles resultados quiere imprimir?")
    d=int(input())
    Diofantica(a,b,c,d)
