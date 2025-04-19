#una excepcion son problemas en el código

#SyntaxError , es problema en el codigo 
#x = int(input("What is x? ))

#ValueError 
#x = int(input("What is x? "))
#print(f"x is {x}")

#estrucuras de control de excepciones
#aqui doy un mensaje de erro al usuario.
#try:
#    x = int(input("What is x? "))
#    print(f"x is {x}") 
#except ValueError:
#    print("X is not an integer")
    
#NameError , haciendo algo un variable que no deberia estar definido

#try:
#    x = int(input("What is x? "))
#except ValueError:
#    print("X is not an integer")

#print(f"x is {x}") #NameError: name 'x' is not defined
#Este problema se da ya que x captura el valor ingresado pero no lo valida y  despues de except quiere
#llamarlo fuera sin su captura o validación con el print

#para solucionar este problema se hace
#try:
#    x = int(input("What is x? "))
#except ValueError:
#    print("X is not an integer")

#print(f"x is {x}")

#else
#try:
#    x = int(input("What is x? "))
#except ValueError:
#    print("X is not an integer")
#else:
#    print(f"x is {x}")
    
#refinando el código
#podemos usar bucles para preguntar lo mismo varias veces
#while True:
#    try:
#        x = int(input("What is x? "))
#    except ValueError:
#        print("X is not an integer")
#    else:
#        break#para salir del bucle 
    
#print(f"x is {x}")    

#tambien podria usar esta solución 
while True:
    try:
        x = int(input("What is x? "))
        break
   
    except ValueError:
        print("X is not an integer")
        
print(f"x is {x}")    


    