from PolinomioMagico import PolinomioMagico
class OperacionesPolinomios:
    @staticmethod
    def restar(p1, p2):
        resultado = p1.terminos.copy()
        for exp, coef in p2.terminos.items():
            resultado[exp] = resultado.get(exp, 0) - coef
            if resultado[exp] == 0:
                del resultado[exp]
        return PolinomioMagico(resultado)

    @staticmethod
    def dividir(p1, p2):
        if not p2.terminos:
            raise ValueError("No se puede dividir por un polinomio vacío.")
        resultado = {}
        dividendo = p1.terminos.copy()
        while dividendo and max(dividendo) >= max(p2.terminos):
            exp_dividendo = max(dividendo)
            exp_divisor = max(p2.terminos)
            coef_dividendo = dividendo[exp_dividendo]
            coef_divisor = p2.terminos[exp_divisor]
            exp_resultado = exp_dividendo - exp_divisor
            coef_resultado = coef_dividendo / coef_divisor
            resultado[exp_resultado] = coef_resultado
            for exp, coef in p2.terminos.items():
                exp_actual = exp + exp_resultado
                dividendo[exp_actual] = dividendo.get(exp_actual, 0) - coef * coef_resultado
                if dividendo[exp_actual] == 0:
                    del dividendo[exp_actual]
        return PolinomioMagico(resultado)

    @staticmethod
    def eliminar_termino(polinomio, exponente):
        if exponente in polinomio.terminos:
            del polinomio.terminos[exponente]

    @staticmethod
    def existe_termino(polinomio, exponente):
        return exponente in polinomio.terminos