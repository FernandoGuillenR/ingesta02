import boto3
import pymysql
import pandas as pd

host_db = "127.0.0.1" 
port_db = 3307 
usuario_db = "root"
password_db = "password123"
nombre_db = "laboratorio"

ficheroUpload = "data.csv"
nombreBucket = "afgr-output-29"

try:
    print("Conectando a MySQL en puerto 3307...")
    conexion = pymysql.connect(
        host=host_db, 
        port=port_db, 
        user=usuario_db, 
        password=password_db, 
        database=nombre_db
    )
    
    # PULL de datos
    df = pd.read_sql("SELECT * FROM ventas", conexion)
    df.to_csv(ficheroUpload, index=False)
    conexion.close()
    print("PULL finalizado. CSV creado.")

    # PUSH a S3
    print(f"Subiendo a {nombreBucket}...")
    s3 = boto3.client('s3')
    s3.upload_file(ficheroUpload, nombreBucket, ficheroUpload)
    print("TODO LISTO. Verifica tu bucket.")

except Exception as e:
    print(f"Error: {e}")
