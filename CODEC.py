#Esqueda Rodriguez, Fabian Alejandro

import string
alfabeto = list(string.ascii_lowercase)

#Codificador
def cifrado_cesar(alfabeto, n, texto):
    texto_cifrado = ""
    for letra in texto:
        if letra in alfabeto:
            indice_actual = alfabeto.index(letra)
            indice_cesar = indice_actual + n
            if indice_cesar > 25:
                indice_cesar -= 25
            texto_cifrado += alfabeto[indice_cesar]
        else:
            texto_cifrado += letra

    return texto_cifrado

#Decodificador
def decodificar_archivo(alfabeto,n,texto):
    texto_decodificado = ""
    for letra in texto:
        if letra in alfabeto:
            indice_cesar = alfabeto.index(letra)
            indice_original = indice_cesar - n
            if indice_original < 0 :
                indice_original += 25
            texto_decodificado += alfabeto[indice_original]
        else:
            texto_decodificado += letra

    return texto_decodificado

print("\n\t\t\tCODEC\n")
print("(1) Codificar un archivo" + '\n')
print("(2) Decodificar un archivo" + '\n')
print("(0) Salir" + '\n')
opcion = int(input("¿Qué acción deseas realizar? "))

while opcion != 0:
    if opcion == 1:
        print("\n\t\t\tCODIFICAR ARCHIVO")
        archivo = open(input("\n\nDame el nombre del archivo a codificar: ") + ".txt", 'r')#Abrir el archivo en modo de lectura

        codificar = archivo.read()#Leer el archivo
        
        archivo_codificado = cifrado_cesar(alfabeto, 1, codificar)#Mandar el archivo para cifrarlo
        
        unstoppable_codificado = open("unstoppable_codificado.txt", 'w')#Abre un archivo en modo de escritura
        unstoppable_codificado.write(archivo_codificado)#Se escribe el texto cifrado

        archivo.close()
        unstoppable_codificado.close()

    elif opcion == 2:
        print('\n\t\tDECODIFICAR ARCHIVO')
        archivo = open(input("\n\nDame el nombre del archivo a decodificar: ") + ".txt", 'r')#Abrir el archivo en modo de lectura

        decodificar = archivo.read()

        archivo_decodificado = decodificar_archivo(alfabeto, 1, decodificar)#Mandar el archivo para decodificarlo

        unstoppable_decodificado = open("unstoppable_decodificado.txt", 'w')#Abre un archivo en modo de escritura
        unstoppable_decodificado.write(archivo_decodificado)#Se escribe el texto cifrado

        archivo.close()
        unstoppable_decodificado.close()

    print("\n\t\t\tCODEC\n")
    print("(1) Codificar un archivo" + '\n')
    print("(2) Decodificar un archivo" + '\n')
    print("(0) Salir" + '\n')
    opcion = int(input("¿Qué acción deseas realizar? "))
