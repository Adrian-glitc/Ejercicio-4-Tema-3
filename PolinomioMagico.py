class PolinomioMagico:
    def __init__(self, terminos=None):
        self.terminos = terminos if terminos else {}

    def __str__(self):
        if not self.terminos:
            return "0"
        return " + ".join(f"{coef}x^{exp}" if exp != 0 else f"{coef}" 
                           for exp, coef in sorted(self.terminos.items(), reverse=True))

    def evaluar(self, x):
        return sum(coef * (x ** exp) for exp, coef in self.terminos.items())