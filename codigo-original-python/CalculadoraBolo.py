import time
import pickle # El módulo pickle implementa un algoritmo para convertir un objeto arbitrario Python en una serie de bytes. 
              # Este proceso es también llamado serialización de objetos.

class control_glucosa():
    alimento = dict()
    guarnicion = dict()
    hora = time.localtime() #extrae la hora actual de la pc
    pickle.dump(alimento,open("Datos_Alimentos.dat","wb"))

    def __init__(self, alimento): #inicializa el objeto
        if any([x == alimento for x in self.alimento]) == False:
            print("El alimento ingresado no se encontro.")

    def corecion(self, nivel_glucosa): #establece la correccion de acuerdo al nivel de glucosa
        if nivel_glucosa >= 20 and nivel_glucosa <80:
            output = "Su nivel de glucosa es bajo."
            valor = 0
        if nivel_glucosa >= 80 and nivel_glucosa < 150:
            output = "Estas en un buen rango!"
            valor = 1
        if nivel_glucosa >= 150 and nivel_glucosa < 200:
            output = "Rango aceptable"
            valor = 2
        if nivel_glucosa >= 200 and nivel_glucosa < 251:
            output = "Demasiado alto!"
            valor = 3
        if nivel_glucosa >= 251 and nivel_glucosa < 300:
            valor = 4
        if nivel_glucosa >= 301:
            valor = 5
        print("\n",output,"\n")
        return valor
            
    def ratio(self,hora,alimento,porciones,guarnicion): #calcula por conteo de carbohidratos.
        if hora.tm_hour >= 0 and hora.tm_hour <= 11:
            conteo = ((self.alimento[alimento]*porciones)+self.guarnicion[guarnicion])/6.98
        elif hora.tm_hour > 11 and hora.tm_hour <= 15:
            conteo = ((self.alimento[alimento]*porciones)+self.guarnicion[guarnicion])/6.98
        elif hora.tm_hour > 15 and hora.tm_hour <= 20:
            conteo = ((self.alimento[alimento]*porciones)+self.guarnicion[guarnicion])/8
        else:
            conteo = ((self.alimento[alimento]*porciones)+self.guarnicion[guarnicion])/8
        return conteo
    
    def add_alimento(self):
        alimento = pickle.load(open("Datos_Alimentos.dat","rb"))
        opcion = input("desea añadir alimento? SI o NO: ")
        if opcion == "SI":
            nuevo_alimento_c = int(input("Introduzca cantidad de carbohidratos: "))
            nuevo_alimento_n = str(input("Introduzca nombre de alimento: "))
            self.alimento[nuevo_alimento_n] = [nuevo_alimento_c]
        pickle.dump(alimento,open("Datos_Alimentos.dat","wb"))

comida = str(input("Introduce tu plato:"))
nivel_glucosa = int(input("Introduce tu valor de glucosa: "))
a = control_glucosa(comida)
a.add_alimento()
if a.alimento[comida] == False:
    print("Este alimento no está en el archivo. Añadir:")
    a.alimento[comida] = int(input("Introduce carbohidratos del nuevo alimento"))

porciones = int(input("Cuantas porciones desea?: "))
guarnic = str(input("Ensalada?: SI o NO: "))
if guarnic == "SI":
    guarnic = str(input("que ensalada desea? "))
else:
    print("No se añadió ensalada.")
    guarnic = "NO"
hora = time.localtime()
print("Se tiene que suministrar:",round(a.corecion(nivel_glucosa) + a.ratio(hora,comida,porciones,guarnic)),"unidades de insulina.")


#reestructurar el código, de forma que solicite el ingreso de nuevos alimentos primero.
#al agregar un alimento desconocido, preguntar si se quiere ingresar a la base de datos.-