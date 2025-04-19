#signos para condicionales 
# < menor
# <= menor o igual
#> mayor
#>= mayor o igual
#== igual
#!= diferente

x = int(input("What is X? "))
y = int(input("What is y? "))

if x < y:
    print(f"{x} es menor que {y}")
elif x == y:
    print(f"{x} es igual que {y}")
elif x > y:
    print(f"{x} es mayor que {y}")
else:
    print("Error en tu validación")
    
#operadores logicos o condicionales 
if x < y or x > y:
    print("X is not equal to Y")
else:
    print("X is equal to Y")
    
#recuerda la sangria(identacion)
score = int(input("Score: "))

if score >= 90 and score <=100:
    print("Grade: A")
elif score >= 80 and score <90:
    print("Grade: B")
elif score >= 70 and score <80:
    print("Grade: C")
elif score >= 60 and score <70:
    print("Grade: D")
else:
    print("Grade: F")

#esto tambien lo puedo hacer asi
if 90 <= score <=100:
    print("Grade: A")
elif  80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
else:
    print("Grade: F")
    
#otra forma y más sencilla
if  score >= 90:
    print("Grade: A")
if score >= 80:
    print("Grade: B")
if score >= 70:
    print("Grade: C")
if score >= 70:
    print("Grade: D")
else:
    print("Grade: F")
    
#usando el valor modulo
j = int(input("What's j:"))

if j % 2 == 0:
    print("El número es par: ")
else:
    print("El numero es primo")
    
    
#creando una funcion usando el BOOL
def main():
    x = int(input("What's x?: "))
    if is_even(x):
        print("Even")#Even significa es par
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
#haciendo una expresion PYTHONICA , es el mismo codigo de arriba
#def is_even(n):
#    return True if n % 2 == 0 else False
#    return n % 2 == 0 # esto es la mas corto
          
main() 

#expresion PYTHONICA , cuando algo solo se puede hacer en python 

