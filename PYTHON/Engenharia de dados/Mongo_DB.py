import pandas  as pd 
from pymongo import MongoClient

# conexão com mongo DB

arquivo = pd.read_json(r"C:\Users\pedro\Downloads\estados.json")

client_mongodb =  MongoClient("mongodb://root:rootpassword@awari-mongodb:27017/?serverSelectionTimeoutMS=5000&connectTimeoutMS=10000&authSource=admin&authMechanism=SCRAM-SHA-256")
db = client_mongodb['exercicios']
collection = db['compras']
arquivo.reset_index(inplace=True)
data_dict = arquivo.to_dict("records") # To_dict é para salvar em dicionarios
collection.insert_many(data_dict)
