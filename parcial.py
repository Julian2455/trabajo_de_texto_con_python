def contar_palabras():
    datos=open("texto.txt","r",encoding="utf-8")
    total=0
    for x in datos.readlines():
        linea=x.split(" ")
        total+=len(linea)
    datos.close()
    return total

def contar_individual():
    datos=open("texto.txt","r",encoding="utf-8")
    palabras={}
    for x in datos.readlines():
        linea=x.split(" ")
        for y in linea:
            if y in palabras:
                palabras[y]+=1
            else:
                palabras[y]=1
    return palabras
        

def separar_palabras():
    articulos=['EL','LA','LOS','LAS','UN','UNA','UNO','UNOS','UNAS']
    conjunciones=['Y','O','PERO','AUNQUE','PORQUE','NI','SI','YA QUE','SINO']
    preposiciones=['A','DE','EN','CON','POR','PARA','ENTRE','HACIA','SIN','SOBRE']
    adverbios=['BIEN','RÁPIDAMENTE','AHORA','MAÑANA','LENTAMENTE','SIEMPRE','NUNCA','PRONTO','LEJOS','CERCA']
    signos_puntuacion=['.',',',';',':','¿','?','!','¡','(',')','[',']','"','-','{','}']
    datos=open("texto.txt","r",encoding="utf-8")
    nuevo=open("nuevotexto.txt","w",encoding="utf-8")
    for x in datos.readlines():
        linea=x.split(" ")
        copia=[]
        linea2=linea
        for x in linea:
            cadena=x.upper()
            copia.append(cadena)
        for y in range(len(linea)):
            if copia[y] in articulos:
                del linea[y]
        nuevo.write(f'{linea}')
    datos.close()
    nuevo.close()



while True:
    print("1 <-- Contar la cantidad de palabras en el texto")
    print("2 <-- Mostrar la cantidad de veces que aparece cada palabra")
    print("3 <-- Crear un nuevo texto eliminando")
    print("4 <-- Mostrar las 10 palabras con mayor frecuencia en el nuevo texto")
    print("5 <-- SALIR\n")
    opc=int(input("Ingrese la opcion: "))
    if opc==1:
        palabra=contar_palabras()
        print(f'El texto tiene {palabra} palabras')
    elif opc==2:
        lista_palabras=contar_individual()
        for x,y in lista_palabras.items():
            print(f'{x}:{y}')
    elif opc==3:
        separar_palabras()
    elif opc==4:
        break
    elif opc==5:
        break
    else:
        print("OPCION NO VALIDA\n")