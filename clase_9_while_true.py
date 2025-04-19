#estos son bucles infinitos de validación para que los datos que se ingresen sean los pedidos

#while True:
#    n = int (input("What's n? "))
#    if n < 0:
#        continue # esta función permite continuar en el bucle hasta que se insete lo pedido
#    else:
#        break #te saca del bucle
    
#otra forma de hacerlo es 
#while True:
#    n = int (input("What's n? "))
#    if n > 0:
#        break
    
#for i in range(n):#pueso usar i o _ es igual
#    print("Meow")
    
#ahora hare una funcion
def main():
    number = get_number()
    meow(number)
    
def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break #rompo el bucle 
    return n #devolver el valor en el codigo
    
def meow(n):
    for i in range(n):
        print("meow")

#main()#comentado para no llamarlo 

students = ["Hermione","Harry","Ron"]

#print(students[0])

#usando for para iterar una lista 
#for student in students: #la variable student puede ser I o _ 
#    print(student)
    
#iterando con números con len
for i in range(len(students)):#len(students), los uso para que me diga cuandos estudiantes hay es decir 3
    #print(students[i]) # imprimo la lista  iterada con for 
    #print(i,students[i]) # imprimo la lista con su posición pero inicia de cero
    print(i+1,students[i])#impirmo la lista pero inicio su posición de 1