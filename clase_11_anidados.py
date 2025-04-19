#repasando clases
#for i in range(3):
#    print("#")

#funciones para crear una torre
#def main():
#    print_colum(3)
    
#def print_colum(heigth):
#    for _ in range(heigth):
#        print("#")
        
#main()

#def main():
#    print_row(4)
    
#def print_row(width):
#    print("?" * width)
        
#main()

#*++++++++++++++++++*************************
#fucionando las funciones de largo y ancho

def main():
    print_squares(8)
    
#def print_squares(size):
#    for i in range(size):#for each row in square
#        for j in range(size):#for each brinch in row
#            print("#", end = "")#print brick
#        print()#final de linea automatico

#mejorando el codigo
def print_squares(size):
    for i in range(size):
        print_row(size)
        
def print_row(width):
    print("#" * width)


   
main()