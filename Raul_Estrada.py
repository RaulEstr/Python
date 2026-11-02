import csv
import re

def calular_descuento(precio: float, porc: float) -> dict:
    """
    Funcion que recibe un precio y un descuento (entre 0 y 100) y devuelve un diccionario
    con el valor descontado y el precio final
    Args:
        precio (float): precio inicial
        porc (float): porcentaje descontado

    Returns:
        dict: diccionario con dos claves, descuento y precio_final y sus respectivos valores
    """
    dicc = {}
    descuento = round(precio * porc / 100,2)
    dicc["descuento"] = descuento
    dicc["precio_final"] = round(precio - descuento,2)
    return dicc

def clasificar_imc(peso: float, altura: float) -> dict:
    """
    Funcion que recibe un peso y una altura y devuelve su IMC y su categoría
    Args:
        peso (float): peso en kg (60, 70...)
        altura (int): altura en metros (1.50, 1.70...)

    Returns:
        dict: diccionario con dos claves, imc y categoria y sus respectivos valores
    """

    dicc = {}
    imc = round(peso / (altura * altura),2)
    dicc["imc"] = imc
    if imc < 18.5:
        dicc["categoria"] = "Bajo peso"
    elif imc < 25:
        dicc["categoria"] = "Normal"
    elif imc < 30:
        dicc["categoria"] = "Sobrepeso"
    else:
        dicc["categoria"] = "Obesidad"    
    return dicc


def es_bisiesto(anio: int) -> bool:
    """
    Funcion que recibe un año y devuelve si es bisiesto o no

    Args:
        anio (int): año

    Returns:
        bool: True si es bisiesto, false si no lo es
    """

    esBisiesto = False
    if anio % 4 == 0:
        esBisiesto = True
        if anio % 100 == 0:
            esBisiesto = False
            if anio % 400 == 0:
                esBisiesto = True

    return esBisiesto

def sumar_digitos(num: int) -> int:
    """
    Funcion que suma todos los digitos de un numero

    Args:
        num (int): numero a sumar sus digitos

    Returns:
        int: suma de todos los digitos
    """
    num = abs(num)
    numStr = str(num)
    numSumado = 0
    for i in numStr:
        numSumado += int(i)

    return numSumado

def contar_vocales(texto: str) -> dict:
    """
    Funcion que recibe un texto y devuelve un diccionario con la cantidad de cada vocal

    Args:
        texto (str): texto del que se van a contar las vocales

    Returns:
        dict: diccionario con claves (a,e,i,o,u) y valores de sus respectivas apariciones en el texto
    """
    dicc = {}
    texto = texto.lower()
    cantA = 0
    cantE = 0
    cantI = 0
    cantO = 0
    cantU = 0
    for i in texto:
        if i == "a":
            cantA += 1
        if i == "e":
            cantE += 1
        if i == "i":
            cantI += 1
        if i == "o":
            cantO += 1
        if i == "u":
            cantU += 1

    dicc["a"] = cantA
    dicc["e"] = cantE
    dicc["i"] = cantI
    dicc["o"] = cantO
    dicc["u"] = cantU

    return dicc

def segundo_mayor(nums: list) -> int:
    """
    Funcion que recibe una lista de numeros y devuelve el segundo mayor

    Args:
        nums (list): lista de numeros

    Returns:
        int | None: segundo numero mayor de la lista o None si no hay dos numeros distintos
    """

    if len(nums) == 0:
        return None
    
    numMax = max(nums)
    while nums.count(numMax) > 0:
        nums.remove(numMax)

    if len(nums) == 0:
        return None
    
    return max(nums)

def agrupar_por_inicial(palabras: list) -> dict:
    """
    Funcion que recibe una lista de palabras y devuelve un diccionario con las palabras
    agrupadas por su inicial

    Args:
        palabras (list): lista de palabras

    Returns:
        dict: diccionario con clave de la primera letra de las palabras y como valor la
            lista de las palabras que empiezan por esa inicial
    """
    dicc = {}

    for palabra in palabras:
        inicial = palabra.lower()[0]
        iniciales = dicc.keys()
        if inicial not in iniciales:
            dicc[inicial] = []

        dicc[inicial].append(palabra)   
        
    return dicc

def leer_csv_ventas(ruta: str) -> dict:
    """
    Funcion que recibe la ruta de un archivo csv de ventas y calcula estadisticas

    Args:
        ruta (str): ruta del archivos csv

    Returns:
        dict: diccionario con claves num_ventas, ingreso_total y producto_top y sus respectivos valores
    """
    dicc = {}

    try:
        with open(ruta, "r", newline="", encoding="utf-8") as f:
            lector = csv.reader(f)
            contFilas = 0
            sumaTotal = 0
            ingresoMax = ["", 0]
            for fila in lector:
                if any(fila):
                    contFilas += 1
                    ingreso = float(fila[1]) * float(fila[2])
                    sumaTotal += ingreso
                    if ingreso > ingresoMax[1]:
                        ingresoMax = [fila[0], ingreso]

            dicc["num_ventas"] = contFilas
            dicc["ingreso_total"] = round(sumaTotal, 2)
            dicc["producto_top"] = ingresoMax[0]
    except FileNotFoundError:
        dicc["error"] = "Archivo no encontrado"

    return dicc

def cifrar_cesar(texto: str, desplazamiento: int) -> str:
    """
    Funcion que recibe un texto y lo devuelve cifrado con el cifrado Cesar

    Args:
        texto (str): texto original
        desplazamiento (int): cantidad de desplazamiento
        
    Returns:
        str: texto cifrado
    """
    lista = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]

    cifrado = ""
    for letra in texto:
        patron = r"[a-z|A-Z|ñ|Ñ]"
        if re.search(patron, letra):
            posNuevaLetra = lista.index(letra.lower()) + desplazamiento
            if posNuevaLetra >= len(lista):
                posNuevaLetra = posNuevaLetra % len(lista)

            patronMayus = r"[A-Z|Ñ]"
            if re.search(patronMayus, letra):
                cifrado += lista[posNuevaLetra].upper()
            else:
                cifrado += lista[posNuevaLetra]   
        else:
            cifrado += letra

    return cifrado

def sumular_cajero(operaciones: list, saldo_inicial: float = 0) -> dict:
    """
    Funcion que recibe una lista de operaciones a realizar y un saldo inicial (por defecto 0), realiza las operaciones
    y devuelve un diccionario con el saldo final, cantidad de operaciones correctas y cantida de operaciones rechazadas

    Args:
        operaciones (list): lista de diccionario de operaciones
        saldo_inicial (float, optional): saldo inicial del cajero. Defaults to 0

    Returns:
        dict: diccionario con claves saldo_final, operaciones_ok y operaciones_rechazadas y sus respectivos valores
    """
    dicc = {}
    saldo = saldo_inicial
    operacionesOK = 0
    operacionesNOT = 0
    for operacion in operaciones:
        if operacion["tipo"] == "ingreso":
            saldo += operacion["cantidad"]
            operacionesOK += 1
        elif operacion["tipo"] == "retiro":
            if saldo - operacion["cantidad"] < 0:
                operacionesNOT += 1
            else:
                saldo -= operacion["cantidad"]
                operacionesOK += 1
        else:
            operacionesNOT += 1

    dicc["saldo_final"] = round(saldo, 2)
    dicc["operaciones_ok"] = operacionesOK
    dicc["operaciones_rechazadas"] = operacionesNOT

    return dicc

if __name__ == "__main__":
    # 1
    print("1----------------------------")
    print(calular_descuento(100, 20))

    # 1
    print("2----------------------------")
    print(clasificar_imc(70, 1.75))

    print("3----------------------------")
    print(es_bisiesto(2024))
    print(es_bisiesto(2023))
    print(es_bisiesto(1900))
    print(es_bisiesto(2000))

    print("4----------------------------")
    print(sumar_digitos(123))
    print(sumar_digitos(-45))
    print(sumar_digitos(0)) 

    print("5----------------------------")
    print(contar_vocales("programacion"))
    print(contar_vocales("murcielago"))
    print(contar_vocales("cdfgbv"))
    print(contar_vocales(""))

    print("6----------------------------")
    print(segundo_mayor([3,1,4,1,5,9,2,6]))
    print(segundo_mayor([10,10,9]))
    print(segundo_mayor([5,5,5]))
    print(segundo_mayor([]))
    print(segundo_mayor([1]))

    print("7----------------------------")
    print(agrupar_por_inicial(["casa", "coche", "perro", "gato"]))
    print(agrupar_por_inicial(["Casa", "coche", "Perro", "gato"]))

    print("8----------------------------")
    print(leer_csv_ventas("ventas.csv"))

    print("9----------------------------")
    print(cifrar_cesar("abc", 3))
    print(cifrar_cesar("HoLa", 3))
    print(cifrar_cesar("abc", 29))
    print(cifrar_cesar("xyz", 3))
    print(cifrar_cesar("¡Me llamo Raul!", 5))

    print("10---------------------------")
    operaciones = [{"tipo": "ingreso", "cantidad": 100},
                   {"tipo": "retiro", "cantidad": 40},
                   {"tipo": "retiro", "cantidad": 80}]
    print(sumular_cajero(operaciones))

