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

tupla_notas = zip(notas_1,notas_2)

notas_alumnos = dict(zip(lista_alumnos,tupla_notas))

promedio_alumnos = {}

promedio_curso = 0

for alumno in lista_alumnos:
    promedio = sum(notas_alumnos[alumno]) / 2
    promedio_alumnos[alumno] = promedio
    promedio_curso += promedio

promedio_curso = promedio_curso / len(lista_alumnos)

maximo = -1
nombre_maximo = ""

for alumno in promedio_alumnos:
    if promedio_alumnos[alumno] > maximo:
        maximo = promedio_alumnos[alumno]
        nombre_maximo = alumno

minimo = 1000
nombre_minimo = ""

for alumno in lista_alumnos:
    nota_minima = min(notas_alumnos[alumno])
    if nota_minima < minimo:
        minimo = nota_minima
        nombre_minimo = alumno

print(notas_alumnos)

print(promedio_alumnos)

print(promedio_curso)

print(f"Maximo promediol: {maximo} Alumno: {nombre_maximo}")

print(f"Nota minima: {minimo} Alumno: {nombre_minimo}")