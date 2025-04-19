#for usando una lista
#for i in [1,2,3]:
#    print("meow")
    
#usando un rango
#for i in range(3):
#    print("Meow") 
    
#mejorando el codigo de arriba cambiando el nombre de la variable ya que no importa
#for _ in range(3):#el nombre de la variable es indiferente _
#    print("Meow") 
    
#print("Gato \n" * 3, end ="")

#bucles con parametros de ingresos
#While True , es un bucle infinito que siempre es True y se usa para valaidaciond e datos
while True:
    n = int (input("What's n? "))
    if n < 0:
        continue # esta función permite continuar en el bucle hasta que se insete lo pedido
    else:
        break #te saca del bucle
