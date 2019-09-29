class GeneradorEstadisticas:
    def calcular(self, cadena):
        if cadena == "":
            return [0]
        else:
            numeros = cadena.split(",")
            numeros = list(map(int, numeros))
            return [len(numeros), min(numeros), max(numeros)]
