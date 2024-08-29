 #### cuo = Cuotas
 #### inter = intereses
 #### deu = deuda
 #### sub = subtotal
 #### inter_mes = Intereses al mes
 #### pag_mensal = Pago mensual
 

 ` ` ` 
Inicio

    Leer Cuotas
    Leer intereses
    Leer deuda
    Mientras Deuda > 0
        Subtotal = Deuda/Cuotas
        Intereses_mes = Subtotal * (intereses/100)
        Pago_mensual = intereses_mes + Subtotal
        Cuotas = Cuotas - 1
        Deuda = Deuda - Subtotal
        Imprimir Pago_mensual
    Si Deuda > 0 
        Repetir mientras
Fin
 ` ` ` 