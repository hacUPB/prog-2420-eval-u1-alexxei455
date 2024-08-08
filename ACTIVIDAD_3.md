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
#### Planteamiento solución.
```
Inicio
escribir "Ingrese la cantidad de registros de velocidad y tiempo: "
leer cantidad_registros

distancia_total = 0

para i en rango(0, cantidad_registros):
  escribir "Ingrese la velocidad"
  leer velocidad
  escribir "Ingrese el tiempo"
  leer tiempo
  distancia = velocidad * tiempo
  distancia_total = distancia

escribir "La distancia total recorrida es: " + distancia_total
Fin
```

# Problema 5
#### Luis está participando en un torneo de bolos y quiere calcular su puntaje total. Tiene una lista de las puntuaciones de cada tiro y necesita sumar los puntos siguiendo las reglas del juego.
#### Planteamiento solución.
```
INICIO
    
    leer lista_puntuaciones
    puntaje_total = 0
    cantidad_tiros = 0
    indice = 0

    IMPRIMIR "Ingrese la cantidad de tiros:"
    leer cantidad_tiros 

    MIENTRAS indice < cantidad_tiros
        IMPRIMIR "Ingrese la puntuación del tiro " + (indice + 1) + ":"
        leer puntuacion
        lista_puntuaciones[indice] <- convertir_a_entero(puntuacion)
        indice <- indice + 1
    FIN MIENTRAS

    
    indice <- 0
    MIENTRAS indice < longitud(lista_puntuaciones)
        puntaje_total <- puntaje_total + lista_puntuaciones[indice]
        indice <- indice + 1
    FIN MIENTRAS

    IMPRIMIR "El puntaje total de Luis es: " + puntaje_total
FIN


