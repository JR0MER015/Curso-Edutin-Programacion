#diccionarios dict, keys and values
#los diccionarios son usados tambien con las bases de datos
#students = {
#    "Hermaione":"Grifindor",
#    "Harry": "Grifindor",
#    "Ron" : "Grifinfor",
#    "Draco" : "Slytherin"
#    }

#print(students)
#print(students["Draco"])

#iterando el diccionario y buscando llaves y valores 
#for student in students:
#    print(f"{student} is from  {students[student]}")
    
#listas de diccionarios 
#***********************************************************
students = [
    {"name":"Hermione", "house" : "Grifindor" , "patronus": "Otter"},#nota con las comas , otter = nutria
    {"name": "Harry","house" : "Grifindor", "patronus" : "Stag" },#stag = ciervo
    {"name": "Ron" , "house": "Grifinfor", "patronus" : "Jack Russell terrier" }, 
    {"name": "Draco" , "house": "Slytherin" , "patronus" : None} 
]

for student in students:
    #print(student["name"])
    print(f"{student["name"]}, is from {student["house"]}, and the patronus is {student["patronus"]}")
    
    
#ordenar los diccionarios 
