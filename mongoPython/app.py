# ? para probar el programa: 
# *1. Ejecutar comando "mongod" en la carpeta del proyecto. (inicia el demonio)
# *2. Abrir otra terminal, ejecutar consulta "python <nombredeapp>.py"
# *  (Si no da error estamos bien)
# *3. Abrir otra terminal, ejecutar comando "mongosh"
# ? test> use <nombredebd>
# ? test> show collections (muestra las colecciones)



from pymongo import MongoClient

MONGO_URI = 'mongodb://localhost'

client = MongoClient(MONGO_URI)
# conexion con base de datos

db = client['SemII'] #almacena la base de datos
collection = db['alimentos'] #almacena la coleccion de la base de datos


#*insertar un documento en la coleccion especificada en la base de datos
#collection.insert_one({"_id": 2 ,"name":"keyboard","price": 300})

# product_one = {"name": "mouse"}
# product_two = {"name": "monitor"}

# #*añadir varios elementos de una vez a la bd
# collection.insert_many([product_one,product_two])

#*encontrar todos los elementos que cumplan con la propiedad entre corchetes
results = collection.find({"Alimento":"Lácteos"})
print(results[0])

#*encontrar un elemento que cumpla con la propiedad
# #? si existen 2 elementos me devuelve 1 solo de ellos
# result = collection.find_one({"name":"mouse"})
# print(result)

#*elimina todos los datos que cumplan con la condicion
#! si se pasa corchetes en blanco se elimina toda la coleccion ({})
#result = collection.delete_many({"price":300})

#*elimina un dato que cumplan con la condicion
#result = collection.delete_one({"name":"monitor"})

# collection.insert_one({"name":"laptop"})

# collection.update_one({"name":"laptop"}, {"$set":{"name":"keyboard","price":300}})

#inc sirve para incrementar el dato numerico (suma el nuevo valor con el actual)
# collection.update_one({"name":"keyboard"}, {"$inc":{"price":330}})
