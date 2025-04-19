#obteniendo un dato del usuario y verificando errores
#while True:
#    try:
#        x = int(input("What is x? "))
#    except ValueError:
#        print("X is not an integer")
#    else:
#        break#para salir del bucle 
    
#print(f"x is {x}")  

#refinando esto mas 
#def main():
#    x = get_int()
#    print(f"x is {x}") 
    
#def get_int():
#    while True:
#        try:
#            x = int(input("What is x? ")) #aqui en vez de la variable x puedo usar return
#        except ValueError:
#            print("X is not an integer")
#        else:
#            break#para salir del bucle ,aqui tammbien puedo usar el return ya que se que el bucle terminara
#    return x
    
#main()

#Pass , pasa el error y el usuario no mida nada
def main():
    x = get_int()
    print(f"x is {x}") 
    
def get_int():
    while True:
        try:
            return  int(input("What is x? ")) #aqui en vez de la variable x puedo usar return
        except ValueError:
            pass#no dice el error
    
main()