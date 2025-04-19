#soy un administrados ,tarea repetitiva de tiempo ,problema generar informes diarios sobre el inventario 
#sobre productos orgánicos 

#scrip para generar informe de inventario

import database #modulo personalizado para acceder a la base de datos

#creo la función
def generar_informe():
    productos = database.obtener_inventario()
    
    for producto in productos:
        
        print(f"Producto:{producto["nombre"]},Stock: {producto["stock"]},Vencimiento:{producto["vencimiento"]}")
        
generar_informe()

#otro escenarío común era la necesidad de actualizar automáticamente la fecha de vencimiento de ciertos productos 
#Utilicé argumentos múltiples para permmitir la actualización de múltiples productos a la vez,
#proporcionando parámetros nombrados para mayor claridad


import database

def actualizar_vencimiento(producto_id, nueva_fecha):
    database.actualizar_fecha_vencimiento(producto_id,nueva_fecha)
    
    print(f"Fecha de vencimiento actualizada para el producto con ID {producto_id}")
    
actualizar_vencimiento("Manzanas",15/3/91)#ingreso los valores de la función