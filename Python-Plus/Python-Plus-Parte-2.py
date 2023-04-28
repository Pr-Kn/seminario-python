import csv

"""
    El archivo log_catedras contiene informacion de la actividad de cada usuario en la catedra.

    Crear una funcion con dos parametros, uno recibe el nombre de usuario y el otro tiene un valor por defecto.

    Abrir el archivo log_catedras y no olvidarse de cerrarlo o usar with.

    Recorrer el csv y guardarme la informacion del usuario en una estructura adecuada.

    La funcion retorna la actividad del usuario ingresado dependiendo del valor del parametro por defecto.
        - Si tiene el valor "Todo" el cual esta por default retorna todas las filas informacion de ese usuario.
        - Si tiene el valor "Explicacion" retorna las filas en las que se accedio a 
        “BigBlueButton: Sala de VC de explicaciones de práctica” en la columna "Contexto del evento".
        - Si tiene el valor "Teoria" retorna las filasa en las que se accedio a 
        "Página: Material de las clases" en la columna "Contexto del evento".
    
    El punto 2 consiste en hacer un print hermoso y resulto ser mas dificil que el punto 1
"""

def conseguir_informacion(usuario,accesos="TODO"):
    funciones_acceso = {
        "TODO": lambda x: x[1] == usuario, 
        "EXPLICACION": lambda x: x[1] == usuario and x[3] == "BigBlueButton: Sala de VC de explicaciones de práctica",
        "TEORIA": lambda x: x[1] == usuario and x[3] == "Página: Material de las clases"
        }
    
    with open("log_catedras.csv","r",encoding="UTF-8") as archivo:
        csvreader = csv.reader(archivo, delimiter=',')
        info_usuario = list(filter(funciones_acceso[accesos.upper()],csvreader))
    return info_usuario

usuario = conseguir_informacion("Magneton")

if len(usuario) != 0:
    espacios = "{:<20}{:<22}{:<}"

    print(f"Usuario: {usuario[0][1]}")
    print("-"*56)
    print(espacios.format("Dia/hora","Recurso Accedido","Dir IP"))
    print("-"*56)

    for linea in usuario:
        abreviado = linea[3].split(" ")
        abreviado = " ".join(abreviado[:2])
        print(espacios.format(linea[0],abreviado,linea[6]))
else:
    print("El usuario que introdujo no tiene informacion registrada en la catedra.")
