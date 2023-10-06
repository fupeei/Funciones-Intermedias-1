x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#cambiar 10 a 15

def cambiar(x):
    y = (x[1])
    if y[0] == 10:
        y[0] = 15
        return(y[0])

cambiar(x)
print(x)

#cambiar apellido Jordan a Bryant

def cambiarapellido(estudiantes):
    nombrecompleto = estudiantes[0]
    apellido = nombrecompleto['last_name']
    if nombrecompleto['last_name'] == 'Jordan':
        nombrecompleto['last_name'] = 'Bryant'
    return(apellido)
    
cambiarapellido(estudiantes)
print(estudiantes)

#cambiar nombre Messi por Andres

def cambiarnombre(directorio_deportes):
    deportes = directorio_deportes['fútbol']
    messi = deportes[0]
    if deportes[0] == 'Messi':
        deportes[0] = 'Andres'
    return(messi)
    
cambiarnombre(directorio_deportes)
print(directorio_deportes)

#cambiar 20 por 30

def cambiar2 (z):
    a = z[0]
    b = a['y']
    if a['y'] == 20:
        a['y'] = 30
    return(b)
    
cambiar2(z)
print(z)

print("--------------")

estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(estudiantes):
    for i in range (0, len(estudiantes)):
        print(estudiantes[i])
    
iterateDictionary(estudiantes)


def iterateDictionary2(estudiantes):
    for estudiante in estudiantes:
        primer_nombre = estudiante['first_name']
        print(primer_nombre)

iterateDictionary2(estudiantes)

def iterateDictionary3(estudiantes):
    for estudiante in estudiantes:
        apellido = estudiante['last_name']
        print(apellido)

iterateDictionary3(estudiantes)

print("--------------")

dojo = {
'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
"""
Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todos listas, imprima el nombre de cada clave junto 
con el tamaño de su lista, y luego imprima los valores asociados dentro de la lista de cada clave. Por ejemplo:
def printInfo(dojo):
"""

def printInfo(dojo):
    for clave in dojo:
        if clave == 'ubicaciones':
            print(len(dojo['ubicaciones']),clave)
            for ciudad in dojo['ubicaciones']:
                print(ciudad)
        else:
            print(len(dojo['instructores']),clave)
            for instructor in dojo['instructores']:
                print(instructor)
            





printInfo(dojo)



