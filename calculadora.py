#Welcome message
print ("Bienvenido a la super calculadora de intereses Acerenzomatic 0.2.beta en Python - Cortesía de Sergio Bianco")

#Function definition

def ratecalculator (f_monto, f_cuotas) :
    if f_cuotas == 1:
      x = f_monto
      print (f"El importe a cobrar es el mismo al ingresado (${x}). Me ejecutaste al pedo")
    elif f_cuotas == 2:
      x = f_monto + (f_monto*9/100)
      y = f_monto*9/100
      print (f"Los intereses ascienden a ${y}, aplicándose una tasa del 4,5% mensual. El importe final a cobrar es ${x}")
    elif f_cuotas > 2:
      x = f_monto + (f_monto*6.7*f_cuotas/100)
      y = f_monto*6.7*f_cuotas/100
      print (f"Los intereses ascienden a ${y}, aplicándose una tasa del 6,7% mensual. El importe final a cobrar es ${x}"),
    else:
      print ("No ingresaste un número de cuotas válido. O le pifiaste o reinventaste la economía")

#Making calculator reusable

repeat = "si"
while repeat == "si":
    #Asking user for input
    monto = input("Ingrese el monto ")
    print (f"El monto ingresado es ${monto}")
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

    calculator = ratecalculator(f_monto, f_cuotas)

#JobDone

    print ("Trabajo finalizado. A mimir hasta recibir nueva orden")

#Asking if user wants to reuse the Calculator

    repeat = input("¿Desea realizar otro cálculo, querido? (si/no)")

print ("Hasta la vista, baby")
