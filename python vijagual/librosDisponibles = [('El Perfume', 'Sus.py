librosDisponibles = [('El Perfume', 'Suskind', 'Misterio'),
                    ('La Metamorfosis', 'Kafka', 'Novela'), 
                    ('Misery', 'Stephen King', 'Misterio'), 
                    ('Harry Potter', 'J.K. Rowling', 'Novela'), 
                    ('El Principito', 'Saint-Exupery', 'Infantil'), 
                    ('El Codigo Da Vinci', 'Dan Brown', 'Misterio')]

clasificacion = input("Digite la clasificación de los libro que desea recibir: ")

respuesta = []
for libro in librosDisponibles:
    if libro[2] == clasificacion :
        respuesta.append(libro[0])

if(len(respuesta) == 0 ):
    print("No se encuentra sobre", clasificacion)
else:
    print(respuesta)