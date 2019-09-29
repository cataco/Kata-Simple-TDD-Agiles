class GeneradorEstadisticas:
    def calcular(self, cadena):
        if cadena == "":
            return [0]
        elif "," not in cadena:
            return [1, int(cadena), int(cadena)]
        else:
            numeros = cadena.split(",")
            return [len(numeros),int(min(numeros))]
