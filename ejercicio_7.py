#validación de datos en una aplicación bancaria

def validar_cantidad_dinero(cantidad):
    #Codigo de validación
    if isinstance(cantidad,(int,float)) and cantidad >= 0:
        #la cantidad es válidada
        return True
        
    else:
        print("Error: La cantidad ingresada no es válida.")
        return False
    
#Integración con la aplicación 

def realizar_transaccion():
    cantidad = float(input("Ingrese la cantidad de dinero a Transferir: "))
    
    if validar_cantidad_dinero(cantidad):
        #continuar con la transacción
        print("Transacción exitosa. !Dinero transferido¡")
        
    else:
        #Manejar el error y volver a solicitar la cantidad
        print("Por favor, ingrese una cantidad válida.")
        
        realizar_transaccion()
        
#realizar_transaccion()

#Iteraciones con listas 
#si se desea validación a una lista de transacciones , se puede realizar un bucle pra iterar sobre
#la lista y aplicar la validación a cada elemento

def validar_transaccion(lista_transacciones):
    for cantidad in lista_transacciones:
        if not validar_cantidad_dinero(cantidad):
            return False
        
    return True

realizar_transaccion()