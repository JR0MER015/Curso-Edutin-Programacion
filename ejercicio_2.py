#optimizando el análisis financiero

#Laura recibe datos financieros en formato cadena . utiliza type para convertir estos datos a valores numéricos 

#Type conversion
monto_cadena = "$1,234.56"
monto_numerico = float(monto_cadena.replace("$"," ").replace(",",""))

print(monto_numerico)

#valores de coma flotante
tasa_interes = 0.05
monto_interes = monto_numerico * tasa_interes
print(f"${round(monto_interes,2)}")

#para presentar informes financieros de manera clara Laura utiliza numeric formating para formatear resultados
#Numeric formatting
monto_formateado = "${:,.2f}".format(monto_interes)
print(monto_formateado) #es lo mismo que el comando round 

#división 
porcentaje_ganacia = monto_interes / monto_numerico * 100
print(f"% {porcentaje_ganacia}")


#definiendo funciones
def calcular_interes(monto,tasa):
    return monto * tasa

interes_calculado = calcular_interes(100,0.05)
print(f"$ {interes_calculado}")

#scope : al gestionar variables dentro de funciones,se asegura de que no haya conflictos de ámbitos
#y los resultados sean coherentes

#scope
def otra_funcion():
    #esta variable es independiente de la variable monto_cadena fuera de la función
    
    variable_local = 10
    
#valores de retorno las funciones devuelven valores significativos que se utilizan para análisis

