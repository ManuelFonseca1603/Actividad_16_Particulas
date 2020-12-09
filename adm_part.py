from .particula import Particula
import json

class Adm_part:
    def __init__(self):
        self .__particula = []     

    def ordenar(self, particula:Particula):
        self.__particula.remove(particula)
        self.__particula.append(particula)    
        
    def agregar_final(self, particula:Particula):
        self.__particula.append(particula)

    def agregar_inicio(self, particula:Particula):
        self.__particula.insert(0,particula)

    def mostrar(self):
        for particula in self.__particula:
            print(particula) 

    def __str__(self):
        return "".join(
            str(particula) + '\n' for particula in self.__particula 
        ) 

    def __len__(self):
        return len(self.__particula) 

    def __iter__(self):
        self.cont = 0

        return self

    def __next__(self):
        if self.cont < len(self.__particula):
            particula = self.__particula[self.cont]
            self.cont += 1 
            return particula
        else:
            raise StopIteration      

    def guardar (self,ubicacion):
        try:   
            with open(ubicacion,'w') as archivo:
                lista = [particula.to_dict() for particula in self.__particula]
                print(lista)  
                json.dump(lista, archivo, indent=5)    
            return 1
        except:
            return 0      


    def abrir (self,ubicacion):
        try:
            with open(ubicacion,'r') as archivo:
                lista = json.load(archivo)
                self.__particula = [Particula(**particula) for particula in lista]
            return 1
        except:
            return 0                    



# l01 = Particula(id=100,origen_x=56,origen_y=34,destino_x=345,destino_y=400,
#                 velocidad=34,red=23,green=123,blue=200,distancia=0)
# l02 = Particula(id=200,origen_x= 100,origen_y= 140,destino_x= 400,destino_y= 440,
#                 velocidad= 120,red= 300,green= 12,blue=0,distancia= 0)

# adm_part = Adm_part()
# adm_part.agregar_final(l01)
# adm_part.agregar_inicio(l02)
# adm_part.agregar_inicio(l01)
#  adm_part.mostrar()