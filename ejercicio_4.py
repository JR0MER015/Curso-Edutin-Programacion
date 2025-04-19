#reservar un hotel con pYTHON y verificar disponibilidd

#verificar si hay disponibilidad , implementar una función que verifique disponibilidad en una fecha
#aseguarnos que la fecha solicitada esta disponible

def verificar_disponibilidad(fecha,habitacion):
    habitacion_disponible = consultar_disponibilidad_habitacion(habitacion)
    fecha_disponible = consultar_disponibilidad_fecha(fecha)
    
    if habitacion_disponible and fecha_disponible:
        return True
    else:
        return False
    
#verifiacion de requisitos de pagos

def verificar_pago(monto_pagado, monto_requerido):
    if monto_pagado != monto_requerido:
        return False
    else:
        True
        
#Integracion de verificaciones 

def realizar_reserva(fecha,habitacion,monto_pagado):
     if verificar_disponibilidad(fecha,habitacion) and verificar_pago(monto_pagado,obtener_precio_habitacion(habitacion)):
         
         confirmar_reserva()
         
         return "Reserva exitos"
     
     else:
        return "Error en la reserva"
    
#este caso no le entendi jajajaja