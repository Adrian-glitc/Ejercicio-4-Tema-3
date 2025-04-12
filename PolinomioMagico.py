class PolinomioMagico:
    def __init__(self, terminos=None):
        # terminos es un diccionario donde la clave es el exponente y el valor es el coeficiente
        self.terminos = terminos if terminos else {}

    def __str__(self):
        if not self.terminos:
            return "0"
        return " + ".join(f"{coef}x^{exp}" if exp != 0 else f"{coef}" 
                           for exp, coef in sorted(self.terminos.items(), reverse=True))