# Algoritmo extendido de Euclides + Solución de ecuaciones diofánticas
Nombre: Emmanuel del Piero Martinez Salcedo

El presente código en python permite encontrar el algoritmo extendido de Euclides y si se desea la solución a la ecuación diofántica

### Algoritmo extendido de Euclides
El algoritmo de Euclides extendido permite, además de encontrar un máximo común divisor de dos números enteros "a" y "b", expresarlo como la mínima combinación lineal de esos números, es decir, encontrar números enteros "x" y "y" tales que ax+by=mcd(a,b). Esto se generaliza también hacia cualquier dominio euclidiano.

### Solución de ecuaciones diofánticas
Se llama ecuación diofántica o ecuación diofantina a cualquier ecuación algebraica, de dos o más incógnitas, cuyos coeficientes recorren el conjunto de los números enteros, de las que se buscan soluciones enteras o naturales, esto es, que pertenezcan al conjunto de los números enteros. Un tipo particular de dichas ecuaciones son las ecuaciones diofánticas lineales con dos incógnitas, las cuales tienen la forma "ax+by=c"

## Funcionamiento
El programa pide ingresar a y b, posterior mente retornara los resultados del algoritmo extendido de Euclides, retornando el mcd, x, y.
Luego preguntara si se desea hallar la solución a una ecuación diofántica, si se ingresa "y" el programa preguntara la solución de esta ecuación diofántica y cuantos resultados posibles se quieren imprimir, al final imprimiendo una serie de x1 y y1

## Código

```python
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
```
