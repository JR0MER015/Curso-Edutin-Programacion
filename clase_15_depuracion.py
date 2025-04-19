#debugging

#primera herramienta es print

#def main():
#    height = int(input("Height: "))
#    pyramid(height)
    
#def pyramid(n):
#    for i in range(n):
#        #print(i,end=" ")#lo coloco es para ver que pasa 
#        print("#"* (i+1))#* solo es para concatenar

#if __name__ == "__main__":
#    main()
 
 #ayudante depurador de debugging
 #breakpoint - ayuda a identificar donde esta el problema
def main():
    height = int(input("Height: "))
    pyramid(height)
    
def pyramid(n):
    for i in range(n):
        #print(i,end=" ")#lo coloco es para ver que pasa 
        print("#"* (i+1))#* solo es para concatenar
        
if __name__ == "__main__":
    main()#para colocar un breakpoint se hace click al lado izquierdo del numero 
    #y para correr el terminal se hace click en el boton de la cucaracha jajaj
    #submenu se abre al ingresar en run and debug 
    #la flecha para abajo es para correr lo de saltar lo usamos para funciones ya dadas por Python
    
