#usando argumentos
def main():
    x = get_int("What's x ? ")
    print(f"x is {x}") 
    
def get_int(prompt):#prompt lo que hace es inmedito es como una captura de lo que ingreso x
    while True:
        try:
            return  int(input(prompt)) #aqui en vez de la variable x puedo usar return
        except ValueError:
            pass#no dice el error
    
main()