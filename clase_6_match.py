#name = input("What's your name: ")

#if name == "Harry":
#    print("Gryffindor")
#elif name == "Hermione":
#    print("Gryffindor")
#elif name == "Ron":
#    print("Ron")
#elif name == "Draco":
#    print("Slytherin")
#else:
#    print("Who?")  
    
#mejorando el codigo
#name = input("What's your name: ")
#if name == "Harry" or name == "Hermione" or name == "Ron" :
#    print("Gryffindor")
#elif name == "Draco":
#    print("Slytherin")
#else:
#    print("Who?")  
    
#hay otra tecnica usada match
#name = input("What's your name: ")

#match name:
#    case "Harry":
#        print("Gryffindor")
#    case "Hermione":
#        print("Gryffindor")
#    case "Ron":
#        print("Gryffindor")
#    case "Draco":
#        print("Slytherin")
#    case _:#se crea un caso para con _ para aquellos casos que no son especificos 
#        print("Who?")
        
#simplificando el codigo a menos lineas 
name = input("What's your name: ")

match name:
    case "Harry"| "Hermione" | "Ron" : 
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:#se crea un caso para con _ para aquellos casos que no son especificos 
        print("Who?")

#sirve para emparejamiento y simplifica el codigo
