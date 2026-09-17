from ej1 import Alumno


class GestorAcademico:
    """Clase que gestiona la base de datos de alumnos con operación CREATE segura."""
    def __init__(self):
        self.__base_datos_alumnos = []  # Lista privada

    def registrar_nuevo_alumno(self, alumno: Alumno):
        """Registra un alumno validando que no exista otro con el mismo DNI."""
        dni_nuevo = alumno.get_dni()

        #Verificar si el DNI ya existe en la base de datos
        for alumno_existente in self.__base_datos_alumnos:
            if alumno_existente.get_dni() == dni_nuevo:
                print(f"ALERTA: El DNI {dni_nuevo} ya se encuentra registrado en el sistema.")
                return False

        # Si no está duplicado, agregar a la base de datos
        self.__base_datos_alumnos.append(alumno)
        print(f"Alumno {alumno.get_nombre()} {alumno.get_apellido()} registrado exitosamente.")
        return True

    def mostrar_alumnos(self):
        """Muestra todos los alumnos registrados."""
        if not self.__base_datos_alumnos:
            print("No hay alumnos registrados.")
        else:
            print("Alumnos registrados:")
            for alumno in self.__base_datos_alumnos:
                print(f"  - {alumno.obtener_informacion()}")


if __name__ == '__main__':
    gestor = GestorAcademico()

    # Crear alumnos de prueba
    alumno1 = Alumno("Juan", "Pérez", 45123456, "4° 3°", 8.5)
    alumno2 = Alumno("María", "López", 40987654, "3° 2°", 9.2)
    alumno3 = Alumno("Pedro", "García", 45123456, "5° 1°", 7.8)  # DNI duplicado

    # Intentar registrar
    gestor.registrar_nuevo_alumno(alumno1)  # Debe agregar
    gestor.registrar_nuevo_alumno(alumno2)  # Debe agregar
    gestor.registrar_nuevo_alumno(alumno3)  # Debe rechazar (DNI duplicado)

    print()
    gestor.mostrar_alumnos()
