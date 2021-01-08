# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 16:16:12 2021

@author: HP
"""

lista = [0, 88, 72 ,22, 16, 14, 90, 35, 47, 6, 68, 12, 10, 54, 41]
lista.sort() #ordena la lista
#primero buscar el punto medio (puntero)
#segundo comprobar si el punto medio es el valor que buscamos 
# tercero si el numero es menor al valor que buscamos aumentamos inicio 1 sobre el puntero
#cuarto si el numero es mayor al valor que buscamos disminuimos el final 1 bajo el puntero
# quinto si inicio es mayor o igual que final entonces el valor no se encuentra la lista
def busqueda_binaria(valor): # metodo de busqueda binaria
    inicio = 0
    final = len(lista) - 1
    while inicio <= final: # agregamos un ciclo para recorrer el inicio hasta llegar la final
        puntero = (inicio + final) // 2 # se divide el inicio y final entre dos va ser igual el puntero
        if valor == lista[puntero]: #si valor es igual a lista puntero
            return puntero# se retorna
        elif valor >  lista[puntero]:# comprobamos si el valor es menor que el numero que buscamos 
            inicio = puntero + 1 # el inicio es igual al puntero si no el numero es mayor se incrementa
        else:# y si no 
            final = puntero - 1 # significa que el numero es menor se decrementa 
    return None# no se devuelve nada

def buscar_valor(valor):# funcion para buscar valor 
    res_busqueda = busqueda_binaria(valor) #se guarga el valor de la busqueda binaria para utilizarla solo una vez
    if res_busqueda is None: # si resultado de busqueda es nada 
        return f"El numero {valor} no se a encontrado" # se retorna si no se encuentra el valor que buscamos
    else: #si no 
        return f"El numero {valor} se encuentra en la posicion: {res_busqueda}"# se retorna el valor que buscamos y la posicion que se encuentra
while True:
    numero = input("Ingrese el numero que deseas buscar: ") # solicitamos el valor del numero que se desea buscar
    print("----------------")
    print(buscar_valor(int(numero)))# se imprime el metodo de buscar
    print("----------------")
    si_no = input('¿Quieres continuar?. "Si" o "no": ') # si encuentra el valor se imprime y vuelve a pedir que si desea buscar mas numeros
    if si_no.lower() == "si": # si le decimos si va volver a pedir que se inserte el valor a buscar
        print("----->>>>>: ")
    elif si_no.lower() == "no": #si no  va salir de la ejecucion
        print("¡ADIOS!")
    else:
        print("Esta opcion no existe")# se imprime el mensaje en cuando no se encuentra el elemento
        break

