import boto3
import pymysql
import pandas as pd

# ---CONFIGURACIÓN MYSQL ---#
db_host = "db"
db_user = "root"
db_pass = "academy_pass"
db_name = "laboratorio"

print("Extrayendo datos de MySQL...")
conexion = pymysql.connect(host=db_host, user=db_user, password=db_pass, database=db_name)

df = pd.read_sql("SELECT * FROM usuarios", conexion)
df.to_csv("data.csv", index=False)
conexion.close()

ficheroUpload = "data.csv"
nombreBucket = "gcr-output-01"

s3 = boto3.client('s3')
response = s3.upload_file(ficheroUpload, nombreBucket, ficheroUpload)
print(response)

print("Ingesta completada")
