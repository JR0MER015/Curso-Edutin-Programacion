#Control de saldo de tienda virtual

#verificar si hay suficiente saldo en una tienda virtual

username = input("Nombre de Usuario: ")

password = input("Contraseña: ")

if username == "usuario123" and password == "contraseña123" :
    print("Usuario y contraseña correcta")
    
else:
    print("Credenciales incorrectas. Vuelve a intentarlo.")
    
    
producto_seleccionado =input("Ingrese el producto seleccionado: ").strip().title()

saldo_usuario = int(input("Ingrese su saldo: "))

if producto_seleccionado == "Laptop" and saldo_usuario >= 1000:
    print("Producto agregado al carrito.")
elif producto_seleccionado == "Tablet" and saldo_usuario >= 500:
    print("Producto agregado al carrito.")
else:
    print("Saldo insuficiente para este producto.")
    
#proceso de compra
Laptop = 1000
Tablet = 500


if producto_seleccionado == "Laptop":
    print(f"Laptop = {Laptop}")
    print(f"Su saldo es :{saldo_usuario - Laptop}")
    saldo_usuario - Laptop

elif producto_seleccionado == "Tablet":
    print(f"Tablet = {Tablet}")
    print(f"Su saldo es: {saldo_usuario - Tablet}")
    saldo_usuario - Tablet
    
else:
    print("We don't have that item")

#validacion final

if saldo_usuario >= 0:
    print("Compra exitosa. ¡Gracias por tu compra!")
    
else:
    print("Fondos insuficientes. Agregar fondos a tu cuenta.")
    
#print(saldo_usuario)