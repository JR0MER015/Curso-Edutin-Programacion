#name = str(input("What is your name?: "))

#remove whitespace from str
#name = name.strip()#quita los espacios en blaco 
#name = name.capitalize()#capitalize solo la primera letra
#name = name.title()#poner en mayuscula todas la primera parte

#tambien puedo unificar metodos asi con strip y title
#name = name.strip().title()

#incluso se puede hacer esto
name = str(input("What is your name?: ")).strip().title() # I love it

#usanso slipt para saludar solo por el apellido
#esto es una maravilla
first_name , second_name , first_lastname, second_lastname = name.split(" ")

print(f"Hello Mr {first_lastname}")
print(f"Hello , {name} , you are great.")
print("Hallo, " + name)
print("Hallo, " , name) #con , tambien concatenamos solo que añade un espacio más

#se puede añadir comillas dentro de comillas
print('Hola, "Amigo"')#puedo usar diferentes comillas entre el texto
print("Hallo, 'friend'")
# otra forma es con caracteres de escape como \"
print("hello, \"friend\"")


