#creación de un formulario de registro para una tienda de equipos informáticos

#creación de un formulario

#nombre = input("Ingrese su nombre: ")
#direccion = input("Ingrese su dirección: ")
#telefono = input("Ingrese su número de teléfono: ")

#implementacion de validaciones

#while not nombre.isalpha() or not direccion or telefono.isdigit():
#    print("!Error¡ Ingrese información valilda")
#    nombre = input("Ingrese su nombre: ")
#    direccion = input("Ingrese su dirección: ")
#    telefono = input("Ingrese su número de teléfono: ")
    
#optimización con la estructura de datos for

campos = ["Nombre","Dirección","Teléfono"]

for campo in campos:
    dato = input(f"Ingrese su {campo}: ")
    
    while not dato.isalpha() or campo == "Teléfono" and not dato.isdigit():
        print(f"!Error¡ Ingrese un {campo} válido.")
        dato = input(F"Ingrese su {campo}: ")
        
#este ultimo no funciona bien hay que mejorarlo
