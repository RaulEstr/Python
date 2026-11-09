## 9. Ejercicio propuesto
from sqlalchemy import create_engine, String, Float, Integer, Boolean, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
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

    def __repr__(self):
        return f"<Libro(Titulo='{self.titulo}', Autor='{self.autor}', Prestado='{self.prestado}')>"

engine = create_engine('sqlite:///biblioteca.db', echo=False)
Base.metadata.create_all(engine)

with Session(engine) as session:
    libros = [
        Libro(titulo="Harry Potter", autor="JK Rowling", anio=1997, genero="Fantasia"),
        Libro(titulo="El Lazarillo de Tormes", anio=1554, genero="Novela"),
        Libro(titulo="El imperio final", autor="Brandon Sanderson", anio=2008, genero="Fantasia")
    ]

    session.add_all(libros)
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

# Una vez realizado, prueba a añadir la siguiente funcionalidad extra:
# - Añade una tabla de Personas.
# - Añade fechas de publicación en los Libros
# - Añade una relación para gestionar el Préstamos de los Libros a las personas, guardando la fecha de préstamo

if __name__ == "__main__":
    todosLosLibros()
    buscarPorAutor("Sanderson")
    buscarPorGenero("Fantasia")
    alternarPrestado("Harry Potter")
    todosLosLibros()