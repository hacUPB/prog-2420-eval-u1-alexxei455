horas = int(input("¿Cuantas horas trabajaste en la semana?:"))
valor_hora = int(input("¿Cuanto vale cada hora?:"))
if horas > 50:
    print("No está permitido")
elif horas > 45:
    pago_total = (valor_hora*40)+(valor_hora*2*5) + (valor_hora-45)*3
elif horas > 40:
    pago_total = (valor_hora*40) + (valor_hora*(hora - 40)*2)
else:
    pago_total = valor_hora * horas
if horas <= 50:
    print(f"El valor a pagar es ${pago_total}")
        
