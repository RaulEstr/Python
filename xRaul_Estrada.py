import statistics
import csv

def calcular_operaciones(a: float, b: float) -> dict :
    """
    Funcion que recibe dos numeros y calcula su suma, resta, multipliacion y division
    
    Args:
        a (float): primer numero
        b (float): segundo numero
    Returns:
        diccionario (dict): {
            "suma": (a + b), 
            "resta": (a - b), 
            "multiplicacion": (a * b), 
            "division": "Error" | (a / b)}
    """
    dicc = {}
    dicc["suma"] = a + b
    dicc["resta"] = a - b
    dicc["multiplicacion"] = a * b
    dicc["potencia"] = a ** b
    if b == 0:
        dicc["division"] = "Error"
    else:
        dicc["division"] = a / b

    return dicc

def analizar_texto(texto: str) -> dict:
    """
    Funcion que recibe un texto y analiza su contenido
    Args:
        texto (str): texto
    Returns:
        diccionario (dict): {
            "longitud": (int) longitud del texto,
            "palabras": (int) cantidad de palabras,
            "mayusculas": (str) texto en mayusculas,
            "minusculas": (str) texto en minusculas,
            "invertido": (str) texto invertido
            }
    """
    dicc = {}

    dicc["longitud"] = len(texto)
    dicc["palabras"] = len(texto.split())
    dicc["mayusculas"] = texto.upper()
    dicc["minusculas"] = texto.lower()
    inverso = ""
    for i in texto:
        inverso = i + inverso
    dicc["invertido"] = inverso

    return dicc

def estadisticas_lista(numeros: list) -> dict:
    """
    Funcion que recibe una lista de números y saca sus estadísticas
    Args:
        numeros (list): lista de números
    Returns:
        diccionario (dict): {
            "max": (int) número más alto,
            "min": (int) número más bajo,
            "promedio": (int) media de los números,
            "pares": (list) lista de números pares
            }
    """
    
    dicc = {}

    if len(numeros) == 0:
        dicc["max"] = None
        dicc["min"] = None
        dicc["promedio"] = 0
        pares = []
        dicc["pares"] = pares
    else:
        dicc["max"] = max(numeros)
        dicc["min"] = min(numeros)
        dicc["promedio"] = statistics.mean(numeros)
        pares = []
        for num in numeros:
            if num % 2 == 0:
                pares.append(num)
        dicc["pares"] = pares

    return dicc

def generar_triangulo(n: int) -> list:
    """
    Funcion que recibe un numero y genera un patrón numérico triangular
    Args:
        n (int): número
    Returns:
        lista (list): lista con su patrón
    """
    lista = []
    if n <= 0:
        return lista

    for x in range(n + 1):
        elemento = ""
        for y in range(x):
            elemento += str(y + 1)
        if elemento != "":
            lista.append(elemento)

    return lista

def es_numero_feliz(n: int) -> bool:
    """
    Funcion que recibe un numero y devuelve si es feliz o no
    Un número es feliz si, al reemplazarlo repetidamente por la suma de los cuadrados de sus dígitos, se llega a 1. Si entra en un ciclo que no incluye el 1, no es feliz.
    Args:
        n (int): número
    Returns:
        esFeliz (bool): "True" si es feliz, "False" si no es feliz
    """

    seguir = True
    esFeliz = False
    nstr = str(n)
    numerosRepes = set()
    while seguir:
        if nstr in numerosRepes:
            esFeliz = False
            seguir = False
            continue

        suma = 0
        for i in nstr:
            num = int(i)
            result = num * num
            suma += result
        
        numerosRepes.add(nstr)
        nstr = str(suma)
        if suma == 1:
            esFeliz = True
            seguir = False

    return esFeliz

def contar_palabras(texto: str) -> dict:
    """
    Función que recibe un texto y cuenta cuantas veces aparece cada palabra
    Args:
        texto (str): texto
    Returns:
        dicconario (dict): diccionario palabra -> nº de veces
    """
    dicc = {}
    texto = texto.lower()
    palabras = texto.split()
    for palabra in palabras:
        dicc[palabra] = texto.count(palabra)

    return dicc

def es_palindromo(texto: str) -> bool:
    """
    Función que recibe un texto e idica si es palíndromo
    Args:
        texto (str): texto
    Returns:
        esPalindromo (bool): True si es palíndromo, False si no es palíndromo
    """
    texto = texto.lower()
    texto = texto.replace(" ", "")
    iIni = 0
    iFin = len(texto) - 1
    esPalindromo = True

    while esPalindromo and iIni < iFin:
        if texto[iIni] != texto[iFin]:
            esPalindromo = False
        iIni += 1
        iFin -= 1

    return esPalindromo

def leer_csv_alumnos(ruta: str) -> dict:
    """
    Función que recibe una ruta y devuelve estadísticas de alumnos

    Args:
        ruta (str): ruta del archivo

    Returns:
        dicconario (dict): {
            "total_alumnos": cantidad total de alumnos,
            "nota_promedio": media de las notas de los alumnos}
        diccionario (dict): {"error": Archivo no encontrado}
    """
    
    dicc = {}

    try:
        with open(ruta, "r", newline="", encoding="utf-8") as f:
            alumnos = 0
            notas = []
            lector = csv.reader(f)
            for fila in lector:
                if any(fila):
                    if fila[1].isnumeric():
                        alumnos += 1
                        notas.append(float(fila[1]))

        if alumnos == 0:
            dicc["error"] = "No hay alumnos"
        else:
            dicc["total_alumnos"] = alumnos
            dicc["nota_promedio"] = statistics.mean(notas)
    except FileNotFoundError:
        dicc["error"] = "Archivo no encontrado"

    return dicc

def gestionar_empleados(empleados: list, operacion: str, id_empleado: int = None, subida: float = None, salario_minimo: float = None) -> dict | list:
    """
    Funcion que recibe una lista de empleados y una operacion
    Si la operacion es "subir_salario" también recibe un id_empleado y una subida
    Si la operacion es "filtrar_por_salario" también recibe un salario_minimo

    Args:
        empleados (list): lista de empleados
        operacion (str): nombre de la operacion
        id_empleado (int, optional): id del empleado al que subir el salario. Defaults to None.
        subida (float, optional): cantidad de salario que se va a sumar al empleado. Defaults to None.
        salario_minimo (float, optional): cantidad de salario por el cual se va a filtrar. Defaults to None.

    Returns:
        dict | list: 
        dict: Un empleado del que se ha realizado en formato diccionario {"id":, "nombre":, "salario":}
        list: Lista de empleados con el salario mayor al salario_minimo en formato [{"id":, "nombre":, "salario":}, {...}]
    """
    
    if operacion == "subir_salario":
        for empleado in empleados:
            if empleado["id"] == id_empleado:
                empleado["salario"] = empleado["salario"] + subida
                return empleado
            return {"error": "El id_empleado no existe"}

    if operacion == "filtrar_por_salario":
        empleadosFiltrados = []
        for empleado in empleados:
            if empleado["salario"] >= salario_minimo:
                empleadosFiltrados.append(empleado)
        return empleadosFiltrados

    return []
    
def evaluar_tres_en_raya(tablero: list) -> str:
    """
    Funcion que recibe un tablero (lista de 9) y devuelve el estado de la partida del 3 en raya
    Args:
        tablero (list): lista de 9 strings, "X", "O", " "
    Returns:
        estado (str): "X" si ha ganado X, "O" si ha ganado O, "Empate" si no ha ganado ninguno, "En juego" si todavía hay espacios en blanco
    """

    ganadoras = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

    for posiciones in ganadoras:
        if tablero[posiciones[0]] == "X" and tablero[posiciones[1]] == "X" and tablero[posiciones[2]] == "X":
            return "X"
        if tablero[posiciones[0]] == "O" and tablero[posiciones[1]] == "O" and tablero[posiciones[2]] == "O":
            return "O"

    for i in tablero:
        if i == " ":
            return "En juego"

    return "Empate"


if __name__ == "__main__":
    # 1
    print("1----------------------------")
    print(calcular_operaciones(10, 2))
    print(calcular_operaciones(5, 0)['division'])
    print()

    # 2
    print("2----------------------------")
    print(analizar_texto("Python es genial"))
    print()

    # 3
    print("3----------------------------")
    print(estadisticas_lista([7, 2, 9, 1, 5, 8, 3]))
    print(estadisticas_lista([]))
    print()

    # 4
    print("4----------------------------")
    print(generar_triangulo(4))
    print()

    # 5
    print("5----------------------------")
    print(es_numero_feliz(19))
    print(es_numero_feliz(4))
    print(es_numero_feliz(7))
    print()

    # 6
    print("6----------------------------")
    print(contar_palabras("  "))
    print(contar_palabras("hola HOLA mundo esto es es una frase MUNDO"))
    print()

    # 7
    print("7----------------------------")
    print(es_palindromo("Anita lava la tina"))  # True
    print(es_palindromo("Hola"))
    print(es_palindromo("aaaa"))
    print()

    # 8
    print("8----------------------------")
    print(leer_csv_alumnos('alumnos.csv')) 
    print(leer_csv_alumnos('archivo_inexistente.csv'))
    print()

    # 9  
    print("9----------------------------")
    empleados = [
        {'id': 1, 'nombre': 'Ana', 'salario': 1900.0},
        {'id': 2, 'nombre': 'Luis', 'salario': 1500.0}
    ]
    empleado = gestionar_empleados(empleados, "subir_salario", id_empleado=1, subida=300)
    print(empleado["salario"])
    aprobados = gestionar_empleados(empleados, "filtrar_por_salario", salario_minimo=2000)
    print(len(aprobados))
    print()

    # 10
    print("10---------------------------")
    print(evaluar_tres_en_raya(["X", "X", "X",
                                " ", " ", " ",
                                " ", " ", " "]))         

    print(evaluar_tres_en_raya(["O", "X", "X",
                                "X", "O", " ",
                                " ", " ", "O"]))     

    print(evaluar_tres_en_raya(["X", "O", "X",
                                "X", "O", "O",
                                "O", "X", "X"]))  

    print(evaluar_tres_en_raya(["X", " ", " ",
                                " ", " ", "O",
                                " ", " ", " "]))
