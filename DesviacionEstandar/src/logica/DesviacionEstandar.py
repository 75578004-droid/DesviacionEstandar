class DesviacionEstandar:
    def __init__(self, datos):
        self.__datos = datos

    def calcular(self):
        if len(self.__datos) == 0:
            return None
        
        if len(self.__datos) == 1:
            return 0.0
        
        promedio = sum(self.__datos) / len(self.__datos)
        suma_cuadrados = sum((x - promedio) ** 2 for x in self.__datos)
        varianza = suma_cuadrados / len(self.__datos)
        return varianza ** 0.5