#crear funciones 
name = str(input("Ingrese su nombre: ")).strip().title()

def hola():
    print(f"Hola, {name}")
    
hola()

#función usando "TO" , se usa para tener un saludo predeterminado
def hello(to = "World"):
    print("Hello,",to)

hello()

nombre = str(input("Ingrese su nombre: ")).strip().title()

hello(nombre)
