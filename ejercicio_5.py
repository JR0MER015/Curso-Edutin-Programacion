#crear un módulo de autenticación para facturación en restaurantes

#modulo de autenticación 


    
#Integracion del módulo de autenticación en el sistema de facturación 

def inicio_sesion():
    usuario = input("Ingrese su usuario: ").strip().title()
    contraseña = input("Ingrese su contraseña: ").strip()
    
    if autenticar(usuario,contraseña):
        print("Inicio de sesión exitoso.Acceso permitido al sistema de facturación.")
    else:
        print("Inicio de sesión fallido.Verifique sus credenciales.")

def autenticar(usuario,contraseña):
    #consultar base de datos de empleados para verificar credenciales
    empleados = {"Burzum":"666","Sanson":"123","Potter":"Arjona"}
    
    if usuario in  empleados and  empleados[usuario] == contraseña:
        return True
    else:
        return False
       
inicio_sesion()