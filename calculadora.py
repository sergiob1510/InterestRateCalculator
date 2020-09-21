print ("Bienvenido a la super calculadora de intereses Acerenzomatic 0.1.alpha en Python")

#Asking user for input
monto = input("Ingrese el monto ")
print (f"El monto ingresado es {monto}")
cuotas = input("Ingrese numero de cuotas ")
print (f"La cantidad de cuotas es {cuotas}")

#Input gets converted to float - If error, calculator shuts down
try:
    f_monto = float(monto)
    f_cuotas = float(cuotas)
except:
    print("Tenés que meter numeritos, no letras, mamerto. Ahora me cierro")
    quit()


#Calculator
if f_cuotas == 1:
  x = f_monto
  print (f"El monto a cobrar es el mismo al ingresado ({x}), me ejecutaste al pedo")
elif f_cuotas == 2:
  x = f_monto + (f_monto*9/100)
  print (f"Se aplica una tasa de interés del 4,5% mensual. El importe a cobrar es {x}")
elif f_cuotas > 2:
  x = f_monto + (f_monto*6.7*f_cuotas/100)
  print (f"Se aplica una tasa de interés de 6,7% mensual. El importe a cobrar es {x}"),
else:
  print ("No ingresaste un número de cuotas válido. O le pifiaste o reinventaste la economía")

# Goodbye
print ("Trabajo finalizado. A mimir")
