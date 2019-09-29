class GeneradorEstadisticas:
    def calcular(self, cadena):
        if cadena == "":
            return [0]
        elif "," not in cadena:
            return [1,int(cadena)]
        else:
            numeros = cadena.split(",")
            return [len(numeros),int(min(numeros[0],numeros[1]))]
