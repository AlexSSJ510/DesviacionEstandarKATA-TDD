import math


class NoSePuedeCalcular(Exception):
    pass


class DesviacionEstandar:
    def __init__(self):
        self.elementos = []

    def agregar_elemento(self, elemento):
        if not isinstance(elemento, (int, float)):
            raise TypeError("El elemento debe ser un número.")
        self.elementos.append(elemento)

    def ingresar_valores(self):
        while True:
            try:
                valor = input("Ingresa un número (o 'salir' para terminar): ")
                if valor.lower() == 'salir':
                    break
                self.agregar_elemento(float(valor))
            except ValueError:
                print("Por favor, ingresa un número válido.")
            except TypeError as e:
                print(e)

    def media(self):
        if len(self.elementos) == 0:
            raise NoSePuedeCalcular("No se puede calcular el promedio de una lista vacía.")

        total = sum(self.elementos)
        return total / len(self.elementos)

    def desviacion_estandar(self):
        if len(self.elementos) == 0:
            raise NoSePuedeCalcular("No se puede calcular la desviación estándar de una lista vacía.")

        if len(self.elementos) == 1:
            return 0.0

        promedio = self.media()
        varianza = sum((x - promedio) ** 2 for x in self.elementos) / len(self.elementos)
        return math.sqrt(varianza)


# Ejemplo de uso
if __name__ == "__main__":
    estadisticas = DesviacionEstandar()
    estadisticas.ingresar_valores()

    try:
        print(f"Promedio: {estadisticas.media()}")
        print(f"Desviación Estándar: {estadisticas.desviacion_estandar()}")
    except NoSePuedeCalcular as e:
        print(e)
