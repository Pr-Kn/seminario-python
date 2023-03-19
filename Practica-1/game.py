from random import choice, randrange
from datetime import datetime

# Operadores posibles
operators = ["+", "-","*","/"]
# Cantidad de cuentas a resolver
times = 5

math_result = 0
win_count = 0
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
for i in range(0, times):
# Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)

    match operator:
        case "+":
            math_result = number_1 + number_2
        case "-":
            math_result = number_1 + number_2
        case "*":
            math_result = number_1 * number_2
        case _:
            math_result = number_1 / number_2
    # Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
    # Le pedimos al usuario el resultado
    result = input("resultado: ")

    if math_result == int(result):
        print("El resultado es correcto")
        win_count += 1
    else:
        print("El resultado es incorrecto")

# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos.")

print(f"De los 5 intentos acertaste {win_count} y fallaste {times - win_count}")