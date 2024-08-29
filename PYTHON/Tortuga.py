#Viajes

presup = int(input("Ingresar presupuesto:"))
costo_km  = 100
distancia = presup / costo_km
if distancia < 1500:
    print("Casa")
elif distancia < 1600:
    print("México")
elif distancia < 2400:
    print ("PV")
elif distancia < 3600:
    print("Acapulco")
else:
    print("Cancun")
    
