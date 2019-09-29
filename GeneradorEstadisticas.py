class GeneradorEstadisticas:
    def calcular(self, cadena):
        if cadena == "":
            return [0]
        elif "," not in cadena:
            return [1,int(cadena),int(cadena),int(cadena)]
        else:
            numeros = cadena.split(",")
            numeros = list(map(int, numeros))
            return [len(numeros), min(numeros), max(numeros), ((numeros[0]+numeros[1])/2)]
