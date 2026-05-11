FROM python:3-slim
WORKDIR /programas/ingesta
# Instalamos las librerías necesarias
RUN pip3 install boto3 pymysql pandas sqlalchemy
COPY . .
CMD [ "python3", "./ingesta.py" ]
