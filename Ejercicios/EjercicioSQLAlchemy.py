## 9. Ejercicio propuesto
from sqlalchemy import create_engine, String, Float, Integer, Boolean, DateTime, ForeignKey, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from datetime import datetime
import os

os.remove("biblioteca.db")
class Base(DeclarativeBase):
    pass

# Crea un sistema para biblioteca con:
# - Libros (título, autor, año, género)
class Libro(Base):
    __tablename__ = "libros"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    titulo: Mapped[str] = mapped_column(String(100), nullable=False)
    autor: Mapped[str] = mapped_column(String(100), nullable=False, default="Anónimo")
    anio: Mapped[int] = mapped_column(Integer, nullable=False)
    genero: Mapped[str] = mapped_column(String(50))
    prestado: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    # - Añade fechas de publicación en los Libros
    fecha_publicacion: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    
    def __repr__(self):
        return f"<Libro(Titulo='{self.titulo}', Autor='{self.autor}', Prestado='{self.prestado}')>"

# - Añade una tabla de Personas.
class Persona(Base):
    __tablename__ = "personas"
    dni: Mapped[str] = mapped_column(String(9), primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    apellido1: Mapped[str] = mapped_column(String(100), nullable=False)
    apellido2: Mapped[str] = mapped_column(String(100), nullable=False)

    def __repr__(self):
        return f"<Persona(DNI='{self.dni}', Nombre='{self.nombre}', Apellido1='{self.apellido1}', Apellido2='{self.apellido2}')>"

# - Añade una relación para gestionar el Préstamos de los Libros a las personas, guardando la fecha de préstamo
class Prestamo(Base):
    __tablename__ = "prestamos"
    persona_id: Mapped[str] = mapped_column(ForeignKey("personas.dni"), primary_key=True)
    libro_id: Mapped[int] = mapped_column(ForeignKey("libros.id"), primary_key=True)
    fecha_prestamo: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now)

    def __repr__(self):
        return f"<Persona(DNI='{self.persona_id}', Libro='{self.libro_id}', fecha='{self.fecha_prestamo}')"
engine = create_engine('sqlite:///biblioteca.db', echo=False)
Base.metadata.create_all(engine)


with Session(engine) as session:
    libros = [
        Libro(id=1, titulo="Harry Potter", autor="JK Rowling", anio=1997, genero="Fantasia", fecha_publicacion=datetime(1997,1,1), prestado=True),
        Libro(id=2, titulo="El Lazarillo de Tormes", anio=1554, genero="Novela", fecha_publicacion=datetime(1554,1,1), prestado=False),
        Libro(id=3, titulo="El imperio final", autor="Brandon Sanderson", anio=2008, genero="Fantasia", fecha_publicacion=datetime(2008,1,1), prestado=True)
    ]

    personas = [
        Persona(dni="11111111A", nombre="pedro", apellido1="garcia", apellido2="garcia"),
        Persona(dni="22222222B", nombre="maria", apellido1="martinez", apellido2="martinez"),
        Persona(dni="33333333C", nombre="paco", apellido1="rodriguez", apellido2="rodriguez")
    ]

    prestamos = [
        Prestamo(persona_id="11111111A", libro_id=3),
        Prestamo(persona_id="22222222B", libro_id=1)
    ]

    session.add_all(libros)
    session.add_all(personas)
    session.add_all(prestamos)
    session.commit()

# - Buscar libros por autor o género
def todosLosLibros():
    with Session(engine) as session:
        stmt = select(Libro)
        libros = session.scalars(stmt).all()
        print("---------------------------------------")
        for libro in libros:
            print(libro)
        print("---------------------------------------")

def buscarPorAutor(autor: str):
    with Session(engine) as session:
        stmt = select(Libro).where(Libro.autor.contains(autor))
        libros = session.scalars(stmt).all()
        print("---------------------------------------")
        for libro in libros:
            print(libro)
        print("---------------------------------------")

def buscarPorGenero(genero: str):
    with Session(engine) as session:
        stmt = select(Libro).where(Libro.genero == genero)
        libros = session.scalars(stmt).all()
        print("---------------------------------------")
        for libro in libros:
            print(libro)
        print("---------------------------------------")

# - Marcar libros como prestados
def alternarPrestado(titulo: str):
    with Session(engine) as session:
        stmt = select(Libro).where(Libro.titulo == titulo)
        libro = session.scalar(stmt)
        if libro:
            libro.prestado = not libro.prestado
            session.commit()

# - Ver libros prestados
def librosPrestados():
    with Session(engine) as session:
        stmt = select(Prestamo)
        prestamos = session.scalars(stmt).all()
        ids = []
        for prestamo in prestamos:
            ids.append(prestamo.libro_id)

        stmt = select(Libro).where(Libro.id.in_(ids))
        libros = session.scalars(stmt).all()
        print("---------------------------------------")
        for libro in libros:
            print(libro)
        print("---------------------------------------")

# - Ver prestamos
def prestamos():
    with Session(engine) as session:
        stmt = select(Prestamo)
        prestamos = session.scalars(stmt).all()
        print("---------------------------------------")
        for prestamo in prestamos:
            print(prestamo)
        print("---------------------------------------")

def prestar(libro, persona):
    with Session(engine) as session:
        stmt = select(Libro).where(Libro.id == libro)
        libro = session.scalar(stmt)
        if libro:
            libro.prestado = not libro.prestado
            prestamo = Prestamo(persona, libro)
            session.add(prestamo)
            session.commit()

def devolver(libro):
    with Session(engine) as session:
        stmt = select(Prestamo).where(Prestamo.libro_id == libro)
        prestamo = session.scalar(stmt)
        if prestamo:
            session.delete(prestamo)
            session.commit()

        stmt = select(Libro).where(Libro.id == libro)
        libro = session.scalar(stmt)
        if libro:
            libro.prestado = not libro.prestado

if __name__ == "__main__":
    print("Funcion de todos los libros")
    todosLosLibros()
    print("Funcion de buscar por autor")
    buscarPorAutor("Sanderson")
    print("Funcion de buscar por genero")
    buscarPorGenero("Fantasia")
    print("Funcion que alterna el prestado")
    alternarPrestado("Harry Potter")
    print("Funcion que vuelve a mostrar todos los libros para ver si se ha prestado")
    todosLosLibros()
    print("Funcion para ver los libros que estan prestados")
    librosPrestados()
    print("Funcion para ver los prestamos")
    prestamos()