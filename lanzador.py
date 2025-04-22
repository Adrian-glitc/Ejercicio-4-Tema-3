from PolinomioMagico import PolinomioMagico
from Operaciones import OperacionesPolinomios
import pygame

# Ejemplo de uso
def leer_polinomio():
    terminos = {}
    print("Introduce los términos del polinomio (formato: exponente coeficiente). Escribe 'fin' para terminar:")
    while True:
        entrada = input("Término: ")
        if entrada.lower() == "fin":
            break
        try:
            exponente, coeficiente = map(int, entrada.split())
            terminos[exponente] = coeficiente
        except ValueError:
            print("Entrada no válida. Usa el formato: exponente coeficiente")
    return PolinomioMagico(terminos)

def graficar_polinomios(p1, p2):
    pygame.init()
    ancho, alto = 800, 600
    pantalla = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Gráfica de Polinomios")
    blanco = (255, 255, 255)
    negro = (0, 0, 0)
    rojo = (255, 0, 0)
    azul = (0, 0, 255)

    pantalla.fill(blanco)
    pygame.draw.line(pantalla, negro, (0, alto // 2), (ancho, alto // 2), 2)  # Eje X
    pygame.draw.line(pantalla, negro, (ancho // 2, 0), (ancho // 2, alto), 2)  # Eje Y

    def graficar_polinomio(polinomio, color):
        puntos = []
        for x in range(-ancho // 2, ancho // 2):
            x_real = x / 20
            y_real = polinomio.evaluar(x_real)
            x_pantalla = ancho // 2 + x
            y_pantalla = alto // 2 - int(y_real * 20)
            puntos.append((x_pantalla, y_pantalla))
        if len(puntos) > 1:
            pygame.draw.lines(pantalla, color, False, puntos, 2)

    graficar_polinomio(p1, rojo)
    graficar_polinomio(p2, azul)

    pygame.display.flip()
    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
    pygame.quit()
    
def main():
    print("Introduce el primer polinomio:")
    p1 = leer_polinomio()
    print("Introduce el segundo polinomio:")
    p2 = leer_polinomio()

    print("\nPolinomio 1:", p1)
    print("Polinomio 2:", p2)

    resta = OperacionesPolinomios.restar(p1, p2)
    print("\nResta:", resta)

    try:
        division = OperacionesPolinomios.dividir(p1, p2)
        print("División:", division)
    except ValueError as e:
        print("Error en la división:", e)

    exponente_eliminar = int(input("\nIntroduce el exponente del término a eliminar del Polinomio 1: "))
    OperacionesPolinomios.eliminar_termino(p1, exponente_eliminar)
    print("Polinomio 1 después de eliminar término:", p1)

    exponente_buscar = int(input("\nIntroduce el exponente del término a buscar en Polinomio 1: "))
    existe = OperacionesPolinomios.existe_termino(p1, exponente_buscar)
    print(f"¿Existe el término x^{exponente_buscar} en Polinomio 1?:", existe)

    graficar_polinomios(p1, p2)
