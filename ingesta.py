import boto3
import pymysql
import pandas as pd
from sqlalchemy import create_engine

# Configuración
host_db = "127.0.0.1" 
port_db = 3307
usuario_db = "root"
password_db = "password123"
nombre_db = "laboratorio"
ficheroUpload = "data.csv"
nombreBucket = "afgr-output-29"

try:
    print("Conectando a MySQL y extrayendo datos...")
    # Usamos SQLAlchemy para evitar el Warning de pandas
    engine = create_engine(ff"mysql+pymysql://{usuario_db}:{password_db}@{host_db}:{port_db}/{nombre_db}")
    
    # PULL: Leer de MySQL
    df = pd.read_sql("SELECT * FROM ventas", engine)
    df.to_csv(ficheroUpload, index=False)
    print("PULL finalizado. CSV creado.")

    # PUSH: Subir a S3
    print(f"Subiendo a {nombreBucket}...")
    s3 = boto3.client('s3')
    s3.upload_file(ficheroUpload, nombreBucket, ficheroUpload)
    print("¡TODO LISTO! Ingesta completada exitosamente.")

except Exception as e:
    print(f"Error: {e}")
