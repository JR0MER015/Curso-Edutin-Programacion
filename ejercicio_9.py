#automatización de la gestión de notas de universidad

#codigo con error en Syntaxis

#def calcular_promedio(notas):
#    suma = sum(notas)
#    promedio = suma / len(notas)
#    return promedio

#calcular_promedio()

#código manejo de excepciones

#def calcular_promedio(notas):
#    try:
#        suma = sum(notas)
#        promedio = suma / len(notas)
#        return promedio
#    except ZeroDivisionError:
#        print("Error: La lista de notas no puede estar vacía.")
#        return 0
    
#calcular_promedio()
#validación de entrada para prevenir errores de valor

notas= []

def ingresar_notas():

    while True:
        try:
            nota = float(input("Ingrese una nota (- 1 para finalizar): "))
            if nota == -1:
                break
            elif 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Error: La nota debe estar entre 0 y 10.")
        except ValueError:
            print("Error: Ingrese un número válido.")
    return notas

notas = ingresar_notas()
print(notas)

def calcular_promedio(notas):
    try:
        suma = sum(notas)
        print(suma)
        promedio = suma / len(notas)
        print(promedio)
        return promedio
    except ZeroDivisionError:
        print("Error: La lista de notas no puede estar vacía.")
        return 0
    
calcular_promedio()