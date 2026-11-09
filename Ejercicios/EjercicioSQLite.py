# 6. Ejercicio propuesto
import sqlite3
conexion = sqlite3.connect("prueba.db")
cursor = conexion.cursor()

# 1. Crear una tabla llamada `cursos` con columnas `id`, `nombre`, `duracion`.
cursor.execute("""
CREATE TABLE IF NOT EXISTS cursos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    duracion INTEGER NOT NULL)
""")
conexion.commit()

# 2. Insertar al menos **3 cursos**.
cursor.execute("INSERT INTO cursos(nombre, duracion) VALUES (?,?)", ("Python", 300))
cursor.execute("INSERT INTO cursos(nombre, duracion) VALUES (?,?)", ("DWES", 900))
cursor.execute("INSERT INTO cursos(nombre, duracion) VALUES (?,?)", ("DWEC", 750))
conexion.commit()

# 3. Mostrar todos los cursos con `fetchall()`.
cursor.execute("SELECT * FROM cursos")
cursos = cursor.fetchall()
for curso in cursos:
    print("ID: {0}, Nombre: {1}, Duración: {2}h".format(curso[0], curso[1], curso[2]))

# 4. Actualizar la duración de uno de ellos.
cursor.execute("UPDATE cursos SET duracion = ? where id = ?", (100, 1))
conexion.commit()

cursor.execute("SELECT * FROM cursos")
cursos = cursor.fetchall()
for curso in cursos:
    print("ID: {0}, Nombre: {1}, Duración: {2}h".format(curso[0], curso[1], curso[2]))

# 5. Eliminar un curso y comprobar que ya no aparece en los resultados.
cursor.execute("DELETE FROM cursos where id in (?)", (1,))
conexion.commit()

cursor.execute("SELECT * FROM cursos")
cursos = cursor.fetchall()
for curso in cursos:
    print("ID: {0}, Nombre: {1}, Duración: {2}h".format(curso[0], curso[1], curso[2]))

cursor.close()