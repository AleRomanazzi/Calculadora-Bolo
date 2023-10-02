from pymongo import MongoClient

MONGO_URI = 'mongodb+srv://facumaidana2001:dCv2uX6kWMtHMnJb@cluster0.pv3bwll.mongodb.net/'
client = MongoClient(MONGO_URI)

db = client['DiabCalc']  # almacena la base de datos
lacteos = db['Lácteos']
azucarados = db['Azucarados']
carnes = db['Carnes']
cereales = db['Cereales']
frutas = db['Frutas']
grasas = db['Grasas']
Huevo = db['Huevo']
miscelaneas = db['Misceláneos']
pescados = db['Pescados']
vegetales = db['Vegetales']

# results = lacteos.find({"Carbohidratos totales (g)": "6.2"})
# print(results[0])


# def buscar():
#     for i in lacteos.find({"Alimentos": "Lácteos"}):
#         print(i)

# for i in lacteos.find({"Alimento": "Lácteos"}):
#     print(i["Nombre"])

# buscar()-
