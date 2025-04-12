from PolinomioMagico import PolinomioMagico
from Operaciones import OperacionesPolinomios
# Ejemplo de uso
def main():
    if __name__ == "__main__":
        p1 = PolinomioMagico({3: 4, 2: 3, 0: 7})  # 4x^3 + 3x^2 + 7
        p2 = PolinomioMagico({2: 1, 0: 2})        # x^2 + 2

        print("Polinomio 1:", p1)
        print("Polinomio 2:", p2)

        resta = OperacionesPolinomios.restar(p1, p2)
        print("Resta:", resta)

        division = OperacionesPolinomios.dividir(p1, p2)
        print("División:", division)

        OperacionesPolinomios.eliminar_termino(p1, 2)
        print("Polinomio 1 después de eliminar término x^2:", p1)

        existe = OperacionesPolinomios.existe_termino(p1, 3)
        print("¿Existe el término x^3 en Polinomio 1?:", existe)