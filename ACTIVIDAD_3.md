# Problema 6
### Se desea saber cuántos años, meses y días tiene actualmente una persona, basándose en su fecha de nacimiento. Además, le gustaría saber si ya ha cumplido años este año o aún no, y si hoy es su cumpleaños para celebrarlo. Cada una de las fechas está conformada por 3 variables: día, mes y año.

#### Planteamiento solución.

```
Inicio
              
        leer dia_n
        leer mes_n
        leer año_n
        leer dia_a
        leer mes_a
        leer año_a    
    
    definir edad = año_a - año_n
    
        si mes_a < mes_n o mes_a = mes_n y dia_a < dia_n
            edad = edad-1
            
        imprimir("la edad de la persona es", + edad)
        
    
    si dia_a = dia_n y mes_a=mes_n y año_a= año n
        imprimir("¡Feliz cumpleaños!")
        
    sino 
        imprimir("Hoy no es su cumpleaños")
Fin
```

# Problema 4
#### María tiene un registro de las velocidades a las que ha conducido su vehículo y el tiempo que ha mantenido cada velocidad. Quiere calcular la distancia total recorrida.

```
Inicio
escribir "Ingrese la cantidad de registros de velocidad y tiempo: "
leer cantidad_registros

distancia_total = 0

para i en rango(0, cantidad_registros):
  escribir "Ingrese la velocidad " + i + ": "
  leer velocidad
  escribir "Ingrese el tiempo " + i + ": "
  leer tiempo
  distancia = velocidad * tiempo
  distancia_total += distancia

escribir "La distancia total recorrida es: " + distancia_total
Fin
```
# Problema de clase

```
Inicio
leer h_estacionamiento

si h_estacionamiento <= 2 entonces
  costo = h_estacionamiento * 5.00
si no 
    si h_estacionamiento <= 5 entonces
  costo = (2 * 5.00) + ((h_estacionamiento - 2) * 4.00)
si no 
    si h_estacionamiento <= 10 entonces
  costo = (2 * 5.00) + (3 * 4.00) + ((h_estacionamiento - 5) * 3.00)
si no
  costo = (2 * 5.00) + (3 * 4.00) + (5 * 3.00) + ((h_estacionamiento - 10) * 2.00)

escribir "El costo total es: " + costo
Fin
```

