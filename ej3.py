from abc import ABC, abstractmethod
from ej1 import Alumno


class EstrategiaGuardado(ABC):
    """Clase base abstracta para estrategias de guardado."""

    @abstractmethod
    def guardar(self, datos):
        pass


class GuardadoMemoria(EstrategiaGuardado):
    """Guardado en memoria RAM temporal."""

    def __init__(self):
        self.__memoria = []

    def guardar(self, datos):
        self.__memoria.append(datos)
        print(f"[MEMORIA] Alumno {datos.get_nombre()} {datos.get_apellido()} guardado en memoria RAM.")

    def obtener_datos(self):
        return self.__memoria


class GuardadoArchivoTXT(EstrategiaGuardado):
    """Guardado persistente en archivo de texto."""

    def __init__(self, archivo="registro_alumnos.txt"):
        self.__archivo = archivo

    def guardar(self, datos):
        with open(self.__archivo, "a", encoding="utf-8") as f:
            f.write(datos.obtener_informacion() + "\n")
        print(f"[ARCHIVO] Alumno {datos.get_nombre()} {datos.get_apellido()} guardado en {self.__archivo}")


class GestorAcademico:
    """Clase que gestiona la base de datos de alumnos con operación CREATE segura."""

    def __init__(self, estrategia: EstrategiaGuardado):
        self.__base_datos_alumnos = []
        self.__estrategia = estrategia  # Inyección de dependencia

    def registrar_nuevo_alumno(self, alumno: Alumno):
        dni_nuevo = alumno.get_dni()

        for alumno_existente in self.__base_datos_alumnos:
            if alumno_existente.get_dni() == dni_nuevo:
                print(f"ALERTA: El DNI {dni_nuevo} ya se encuentra registrado en el sistema.")
                return False

        self.__base_datos_alumnos.append(alumno)
        print(f"Alumno {alumno.get_nombre()} {alumno.get_apellido()} registrado exitosamente.")

        # Delegar al guardado configurado (polimorfismo)
        self.__estrategia.guardar(alumno)
        return True

    def mostrar_alumnos(self):
        if not self.__base_datos_alumnos:
            print("No hay alumnos registrados.")
        else:
            print("Alumnos registrados:")
            for alumno in self.__base_datos_alumnos:
                print(f"  - {alumno.obtener_informacion()}")


if __name__ == '__main__':
    print("=== ESTRATEGIA: MEMORIA ===")
    gestor_memoria = GestorAcademico(GuardadoMemoria())
    gestor_memoria.registrar_nuevo_alumno(Alumno("Juan", "Pérez", 45123456, "4° 3°", 8.5))
    gestor_memoria.registrar_nuevo_alumno(Alumno("María", "López", 40987654, "3° 2°", 9.2))
    gestor_memoria.registrar_nuevo_alumno(Alumno("Pedro", "García", 45123456, "5° 1°", 7.8))

    print("\n=== ESTRATEGIA: ARCHIVO TXT ===")
    gestor_archivo = GestorAcademico(GuardadoArchivoTXT())
    gestor_archivo.registrar_nuevo_alumno(Alumno("Carlos", "Ruiz", 38765432, "2° 1°", 7.0))
    gestor_archivo.registrar_nuevo_alumno(Alumno("Ana", "Martín", 42111222, "4° 2°", 9.0))

    print("\n=== CONTENIDO DEL ARCHIVO ===")
    try:
        with open("registro_alumnos.txt", "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("No existe el archivo aún.")
