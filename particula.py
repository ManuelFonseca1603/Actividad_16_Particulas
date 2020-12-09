from .algoritmos import distancia_euclidiana

class Particula:
    def __init__(self,id=0,origen_x=0,origen_y=0,destino_x=0,destino_y=0,
                velocidad=0,rojo=0,verde=0,azul=0,distancia=0):
        self.__id = id
        self.__origen_x = origen_x
        self.__origen_y = origen_y
        self.__destino_x = destino_x
        self.__destino_y = destino_y
        self.__velocidad = velocidad
        self.__rojo = rojo
        self.__verde = verde
        self.__azul = azul
        self.__distancia = distancia_euclidiana(origen_x, origen_y, destino_x, destino_y)

    def __str__(self):
        return (
            'ID: ' + str(self.__id) + '\n' +
            'Origen en x: ' + str(self.__origen_x) + '\n' +
            'Origen en y: ' + str(self.__origen_y) + '\n' +
            'Destino en x: ' + str(self.__destino_x) + '\n' +
            'Destino en y: ' + str(self.__destino_y) + '\n' +
            'Velocidad: ' + str(self.__velocidad) + ' m/s \n' +
            'Rojo: ' + str(self.__rojo) + '\n' +
            'Verde: ' + str(self.__verde) + '\n' +
            'Azul: ' + str(self.__azul) + '\n' +
            'Distancia: ' + str(self.__distancia) + '\n' 
        )

    @property
    def id(self):
        return self.__id  

    @property
    def origen_x(self):
        return self.__origen_x  

    @property
    def origen_y(self):
        return self.__origen_y

    @property
    def destino_x(self):
        return self.__destino_x

    @property
    def destino_y(self):
        return self.__destino_y

    @property
    def velocidad(self):
        return self.__velocidad

    @property
    def rojo(self):
        return self.__rojo

    @property
    def verde(self):
        return self.__verde

    @property
    def azul(self):
        return self.__azul

    @property
    def distancia(self):
        return self.__distancia        

    def to_dict(self):
        return{
            "id": self.__id,
            "origen_x": self.__origen_x,
            "origen_y": self.__origen_y,
            "destino_x": self.__destino_x,
            "destino_y": self.__destino_y,
            "velocidad": self.__velocidad,
            "rojo": self.__rojo,
            "verde": self.__verde,
            "azul": self.__azul
        }    

# l01 = Particula(id=100,origen_x=56,origen_y=34,destino_x=345,destino_y=400,
#                 velocidad=34,red=23,green=123,blue=200,distancia=0)
# print(l01)
# l02 = Particula(id=100,origen_x=156,origen_y=134,destino_x=45,destino_y=409,
#                 velocidad=34,red=23,green=123,blue=200,distancia=0)
# print(l02)