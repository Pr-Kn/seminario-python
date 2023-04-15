def crear_diccionario_alumnos(lista,primera_nota,segunda_nota):
    tupla_notas = zip(primera_nota,segunda_nota)
    return dict(zip(lista,tupla_notas))

def promedio(iterable):
    return sum(iterable) / len(iterable)

def crear_diccionario_promedios(diccionario_alumnos):
    promedio_alumnos = {}
    for alumno in diccionario_alumnos:
        promedio_alumnos[alumno] = promedio(diccionario_alumnos[alumno])
    return promedio_alumnos

def promedio_del_curso(diccionario_promedios):
    nota_total = promedio(diccionario_promedios.values())
    return f"Nota promedio del curso: {nota_total}"

def maximo_promedio(diccionario_promedios):
    nombre = max(diccionario_promedios,key=diccionario_promedios.get)
    nota = max(diccionario_promedios.values())
    return f"Promedio maximo\nAlumno: {nombre}\nNota: {nota}"

def nota_minima(diccionario_alumnos):
    nombre = min(diccionario_alumnos,key=diccionario_alumnos.get)
    nota = min(min(diccionario_alumnos.values()))
    return f"Promedio maximo\nAlumno: {nombre}\nNota: {nota}"

nombres = ''' 
    'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
    'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
    'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
    'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
    'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
    'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
    'Yanina' 
    '''

notas_1 = [
    81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
    12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
    85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74
    ]

notas_2 = [
    30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
    64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
    95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 10
    ]

lista_alumnos = nombres.split(",")

lista_alumnos = [alumno.strip("'\n ") for alumno in lista_alumnos]

notas_alumnos = crear_diccionario_alumnos(lista_alumnos,notas_1,notas_2)

promedio_alumnos = crear_diccionario_promedios(notas_alumnos)

promedio_total = promedio_del_curso(promedio_alumnos)

alumno_maximo = maximo_promedio(promedio_alumnos)

alumno_minimo = nota_minima(notas_alumnos)

print(notas_alumnos)

print(promedio_alumnos)

print(promedio_total)

print(alumno_maximo)

print(alumno_minimo)