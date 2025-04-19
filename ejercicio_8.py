#reservar tu asiento en soft-world

#consideramos que el teatro es con tres secciones a,b,c y cada sección tiene 10 filas enumeradas del 
# 1 al 10 , se decide representar la disponibilidad de asientos utilizando un diccionario de listas.
teatro ={
    "A": [True] * 10,
    "B":[True] * 10,
    "C":[True] * 10
}

#
seccion_reservada = "B"
fila_reservada = 3

teatro[seccion_reservada][fila_reservada-1]= False

#con este código se puede visualizar la disponibilidad de asientos en teatros si un asiento está disponible,
#se muestra como disponible , de lo contrario se muestra como ocupado

for seccion, filas in teatro.items():
    print(f"Sección {seccion}: ")
    for fila, disponibilidad in enumerate(filas,start=1):
        estado = "Disponibilidad" if disponibilidad else "Ocupado"
        
        print(f"Fila {fila}: {estado}")
        
    print("\n")
    
#ahora cuando un usuario desea reservar un asiento en la sección B fila 3 actualiza el diccionario para reflejar
#la reserva

