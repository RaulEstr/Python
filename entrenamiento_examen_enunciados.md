# Entrenamiento para el examen de Python

**Módulo:** Optativa – Python (PYTH)
**Ciclo:** Desarrollo de Aplicaciones Web (DW2)
**1ª Evaluación**

Este cuaderno de entrenamiento es **parecido al examen real**: todas las soluciones se escriben como **funciones** para poder comprobarlas con tests unitarios. Sirve para ver el nivel y prepararse.

---

## Instrucciones generales

- Crea un script de Python con tu nombre y apellidos: `<Nombre>_<Apellido1>.py`.
- **Todas las funciones deben incluir un docstring** que explique qué hace, qué recibe y qué devuelve.
- Se valorará el uso correcto de **type hints** (anotaciones de tipo).
- Cada ejercicio es **una función independiente**. Respeta el nombre exacto que se indica.
- Prueba tu función con los ejemplos y con los **casos límite** que se describen.

> **Consejo**: no memorices; entiende cada patrón (recorrer una lista, contar con un diccionario, detectar un ciclo con un set...). En el examen cambian los datos, no la idea.

---

## Ejercicio 1: `calcular_operaciones`

Crea una función que realice operaciones matemáticas básicas con dos números.

- **Parámetros:** dos números `a` y `b`.
- **Retorna:** un diccionario con las claves `suma`, `resta`, `multiplicacion`, `division` y `potencia`.
- **Manejo de errores:** si `b` es 0, la división debe devolver `"Error"` (el resto de operaciones se calculan igual).

**Ejemplo de uso:**

```python
resultado = calcular_operaciones(10, 2)
print(resultado)
# {'suma': 12, 'resta': 8, 'multiplicacion': 20, 'division': 5.0, 'potencia': 100}

resultado2 = calcular_operaciones(5, 0)
print(resultado2['division'])
# "Error"
```

**Casos límite a probar:** `b = 0`, números negativos, números decimales.

---

## Ejercicio 2: `analizar_texto`

Crea una función que analice un texto y devuelva estadísticas básicas.

- **Parámetro:** un string `texto`.
- **Retorna:** un diccionario con: `longitud` (nº de caracteres), `palabras` (nº de palabras), `mayusculas`, `minusculas` e `invertido` (el texto al revés).

**Ejemplo de uso:**

```python
resultado = analizar_texto("Python es genial")
print(resultado)
# {'longitud': 16, 'palabras': 3, 'mayusculas': 'PYTHON ES GENIAL',
#  'minusculas': 'python es genial', 'invertido': 'laineg se nohtyP'}
```

**Casos límite a probar:** texto vacío, varias palabras, una sola palabra.

---

## Ejercicio 3: `estadisticas_lista`

Crea una función que procese una lista de números y calcule estadísticas.

- **Parámetro:** una lista de números `numeros`.
- **Retorna:** un diccionario con: `max`, `min`, `promedio` y `pares` (lista de números pares).
- **Lista vacía:** `max` y `min` valen `None`, `promedio` vale `0` y `pares` es una lista vacía.

**Ejemplo de uso:**

```python
resultado = estadisticas_lista([7, 2, 9, 1, 5, 8, 3])
print(resultado)
# {'max': 9, 'min': 1, 'promedio': 5.0, 'pares': [2, 8]}

resultado2 = estadisticas_lista([])
print(resultado2)
# {'max': None, 'min': None, 'promedio': 0, 'pares': []}
```

**Casos límite a probar:** lista vacía, un solo elemento, todos pares, números negativos.

---

## Ejercicio 4: `generar_triangulo`

Crea una función que genere un patrón numérico triangular.

- **Parámetro:** un número entero `n` (filas del patrón).
- **Retorna:** una lista de strings, donde la fila `i` contiene los números del `1` al `i` seguidos.
- Si `n` es 0 o negativo, devuelve una lista vacía.

**Ejemplo de uso:**

```python
resultado = generar_triangulo(4)
print(resultado)
# ['1', '12', '123', '1234']
```

**Casos límite a probar:** `n = 0`, `n = 1`, `n` negativo.

---

## Ejercicio 5: `es_numero_feliz`

Crea una función que determine si un número es **"feliz"**.

**Definición:** un número es feliz si, al reemplazarlo repetidamente por la suma de los cuadrados de sus dígitos, se llega a 1. Si entra en un ciclo que no incluye el 1, no es feliz.

- **Parámetro:** un número entero `n`.
- **Retorna:** `True` si es feliz, `False` en caso contrario.

**Ejemplo:** 19 es feliz porque `1² + 9² = 82 → 8² + 2² = 68 → 6² + 8² = 100 → 1² + 0² + 0² = 1`.

```python
print(es_numero_feliz(19))  # True
print(es_numero_feliz(4))   # False
print(es_numero_feliz(7))   # True
```

**Casos límite a probar:** `1` (feliz), `4` (no feliz), `0` (no feliz), números grandes.

> **Ayuda:** guarda los números ya vistos en un `set` para detectar cuándo entras en un ciclo.

---

## Ejercicio 6: `contar_palabras`

Crea una función que cuente cuántas veces aparece cada palabra en un texto.

- **Parámetro:** un string `texto`.
- **Retorna:** un diccionario `palabra -> nº de veces`. Cuenta en minúsculas y separando por espacios.

**Ejemplo de uso:**

```python
resultado = contar_palabras("Hola hola mundo")
print(resultado)
# {'hola': 2, 'mundo': 1}
```

**Casos límite a probar:** texto vacío, palabras repetidas, mayúsculas y minúsculas mezcladas.

---

## Ejercicio 7: `es_palindromo`

Crea una función que indique si un texto es un **palíndromo** (se lee igual al derecho y al revés).

- **Parámetro:** un string `texto`.
- **Retorna:** `True` o `False`.
- **Importante:** ignora mayúsculas y espacios.

```python
print(es_palindromo("Anita lava la tina"))  # True
print(es_palindromo("Hola"))                 # False
```

**Casos límite a probar:** texto vacío, una sola letra, mayúsculas y espacios.

---

## Ejercicio 8: `leer_csv_alumnos`

Crea una función que lea un fichero CSV con nombres y notas, y devuelva estadísticas.

- **Formato del fichero:** cada línea `nombre,nota`.
- **Parámetro:** la ruta del fichero `ruta`.
- **Retorna:** un diccionario con `total_alumnos` y `nota_promedio`.
- **Manejo de errores:** si el archivo no existe, devuelve `{'error': 'Archivo no encontrado'}`.

> **Recomendación:** abre el fichero con `with open(ruta, "r") as archivo:` para que se cierre automáticamente al terminar.

**Ejemplo de fichero (`alumnos.csv`):**

```
Ana,25
```

(En este caso las "notas" son edades, pero el proceso es el mismo.)

```
Ana,7
Luis,4
Maria,9
Carlos,6
```

**Ejemplo de uso:**

```python
resultado = leer_csv_alumnos('alumnos.csv')
print(resultado)
# {'total_alumnos': 4, 'nota_promedio': 6.5}

resultado2 = leer_csv_alumnos('archivo_inexistente.csv')
print(resultado2)
# {'error': 'Archivo no encontrado'}
```

**Casos límite a probar:** archivo inexistente, archivo vacío, líneas vacías.

---

## Ejercicio 9: `gestionar_empleados`

Crea una función que gestione una lista de empleados con varias operaciones.

- **Estructura de cada empleado:**

```python
empleados = [
    {'id': 1, 'nombre': 'Ana', 'salario': 2000.0},
    {'id': 2, 'nombre': 'Luis', 'salario': 1500.0}
]
```

- **Parámetros:**
  - `empleados`: la lista de empleados.
  - `operacion`: `"subir_salario"` o `"filtrar_por_salario"`.
  - `id_empleado`, `subida`: para `"subir_salario"`.
  - `salario_minimo`: para `"filtrar_por_salario"`.

- **Operaciones:**
  - `"subir_salario"`: suma `subida` al salario del empleado con ese `id`. Devuelve el empleado modificado.
  - `"filtrar_por_salario"`: devuelve la lista de empleados con `salario >= salario_minimo`.
- **Manejo de errores:** si el `id` no existe o la operación no es válida, devuelve `{'error': ...}`.

**Ejemplo de uso:**

```python
empleados = [{'id': 1, 'nombre': 'Ana', 'salario': 2000.0}]

empleado = gestionar_empleados(empleados, "subir_salario", id_empleado=1, subida=300)
print(empleado['salario'])
# 2300.0

aprobados = gestionar_empleados(empleados, "filtrar_por_salario", salario_minimo=2000)
print(len(aprobados))
# 1
```

**Casos límite a probar:** id inexistente, operación no válida, lista vacía.

---

## Ejercicio 10: `evaluar_tres_en_raya`

Adaptado del juego del tema de juegos. Crea una función que evalúe el estado de un tablero de tres en raya.

- **Parámetro:** `tablero`, una lista de **9 posiciones** con `"X"`, `"O"` o `" "` (espacio = vacío).
- **Retorna:**
  - `"X"` si gana X,
  - `"O"` si gana O,
  - `"Empate"` si está lleno y no gana nadie,
  - `"En juego"` si todavía quedan casillas y nadie ha ganado.

```python
print(evaluar_tres_en_raya(["X", "X", "X",
                            " ", " ", " ",
                            " ", " ", " "]))          # "X"

print(evaluar_tres_en_raya(["O", "X", "X",
                            "X", "O", " ",
                            " ", " ", "O"]))          # "O"

print(evaluar_tres_en_raya(["X", "O", "X",
                            "X", "O", "O",
                            "O", "X", "X"]))          # "Empate"

print(evaluar_tres_en_raya([" ", " ", " ",
                            " ", " ", " ",
                            " ", " ", " "]))
# "En juego"
```

**Casos límite a probar:** victoria en fila, columna y diagonal; empate; partida en curso.

---

## Baremo orientativo

| Ejercicio | Puntos |
|-----------|-------:|
| 1. `calcular_operaciones` | 1.0 |
| 2. `analizar_texto` | 1.0 |
| 3. `estadisticas_lista` | 1.0 |
| 4. `generar_triangulo` | 1.0 |
| 5. `es_numero_feliz` | 1.2 |
| 6. `contar_palabras` | 1.0 |
| 7. `es_palindromo` | 0.8 |
| 8. `leer_csv_alumnos` | 1.2 |
| 9. `gestionar_empleados` | 1.0 |
| 10. `evaluar_tres_en_raya` | 0.8 |
| **TOTAL** | **10.0** |
