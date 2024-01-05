import json
from utilidades import promedio

def pruebas():
    #abre el archivo json
    with open("proyecto/estudiantesinscritos.json", "r") as file:
        
        #variable del archivo json
        data = json.load(file)
    #lista de estudiantes aprobados    
    estudiantesaprobados= {
        
    }
    #id del estudiante a aprobar
    id= str(input("ingrese el id del estudiante: "))
    
    for camper in data["campers"]:
        if camper["ident"] == id:
            notateorica= int(input("ingrese la nota de la prueba teorica: "))
            notapractica= int(input("ingrese la nota de la prueba practica: "))    
            promedio = promedio(notateorica, notapractica)
            
            if promedio >= 60:
                print("estudiante aprobado")
                estudiantesaprobados.append(id)
                
            elif promedio < 60: 
                print("estudiante no aprobado")               
            break
        
        else:
            print("El id del estudiante no existe.") 
        
    with open("proyecto/estudiantesinscritos.json", "w") as file: 
        data["estudiantesaprobados"]= estudiantesaprobados
        json.dump(data, file, indent=1)
    
pruebas()