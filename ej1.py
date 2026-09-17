class Persona:
    """Clase base que representa a una persona con atributos encapsulados."""
    def __init__(self, nombre: str, apellido: str, dni: int):
        self._nombre = nombre        # Atributo protegido
        self._apellido = apellido    # Atributo protegido
        self._dni = dni              # Atributo protegido

    # Getters para acceso seguro
    def get_nombre(self) -> str:
        return self._nombre

    def get_apellido(self) -> str:
        return self._apellido

    def get_dni(self) -> int:
        return self._dni


class Alumno(Persona):
    """Clase Alumno que hereda de Persona e incorpora atributos académicos."""
    def __init__(self, nombre: str, apellido: str, dni: int, curso: str, promedio: float):
        super().__init__(nombre, apellido, dni)
        self._curso = curso          # Atributo específico protegido
        self._promedio = promedio    # Atributo específico protegido

    def get_curso(self) -> str:
        return self._curso

    def get_promedio(self) -> float:
        return self._promedio

    def obtener_informacion(self) -> str:
        return (f"Alumno: {self.get_nombre()} {self.get_apellido()} | DNI: {self.get_dni()} "
                f"| Curso: {self._curso} | Promedio: {self._promedio}")

# --- Prueba del Ejercicio 1 ---
if __name__ == '__main__':
    alumno_prueba = Alumno("Juan", "Pérez", 45123456, "4° 3°", 8.5)
    print(alumno_prueba.obtener_informacion())