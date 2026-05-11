import boto3
import pymysql
import pandas as pd

# Configuración
db_host = "localhost"
db_user = "root"
db_pass = "password123"
db_name = "laboratorio"

# 1. PULL de MySQL (El corazón del Ejercicio 3)
print("Conectando a MySQL para leer los registros...")
conexion = pymysql.connect(host=db_host, user=db_user, password=db_pass, database=db_name)

# Leemos la tabla que acabamos de llenar con tu csv
df = pd.read_sql("SELECT * FROM ventas", conexion)

# Lo guardamos en un nuevo archivo (Ingesta de MySQL a CSV)
fichero_destino = "data_mysql_salida.csv"
df.to_csv(fichero_destino, index=False)
conexion.close()

# 2. PUSH a S3 (Tu código base)
nombreBucket = "gcr-output-01" # Reemplaza con el tuyo

s3 = boto3.client('s3')
s3.upload_file(fichero_destino, nombreBucket, fichero_destino)

print(f"Archivo {fichero_destino} generado desde MySQL y subido a S3.")
