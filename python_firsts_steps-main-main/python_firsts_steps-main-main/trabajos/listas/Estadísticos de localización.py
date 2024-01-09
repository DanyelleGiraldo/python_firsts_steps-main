def mediaritmetica(lista):
   promedio= sum(lista)/len(lista)
   return promedio

def mediaarmonica(lista):
    suma_inversos = sum(1/x for x in lista)
    media_arm = len(lista) / suma_inversos
    return media_arm

def mediana(lista):
    longitud = len(lista)

    if len(lista) %2 !=0:
        lista.sort()
        mediana_impar = lista[longitud // 2]
        return mediana_impar
    elif len(lista) % 2 ==0:
        indice_mediana1 = longitud // 2 - 1
        indice_mediana2 = longitud // 2
        valor_mediana1 = lista[indice_mediana1]
        valor_mediana2 = lista[indice_mediana2]
        mediana_par = (valor_mediana1 + valor_mediana2) / 2
        return mediana_par
    
def modas(lista): 
    contador = Counter(lista)
    dato_mas_repetido = max(contador, key=contador.get)
    return dato_mas_repetido
        

datos= []

x= int(input("cuantos datos va a ingresar?: "))

for i in range(x):
    l= int(input("ingrese sus datos: "))
    datos.append(l)
    
print(mediaritmetica(datos))
print(mediaarmonica(datos))
print(mediana(datos))
print(modas(datos))