FROM python:3.9
MAINTAINER Óscar García <oscar.gpoblacion@uah.es>

WORKDIR /app

# Copiamos el archivo requirements.txt dentro de la imagen del contenedor. 
# El contenido de este archivo se explica más adelante
COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

# Copiamos la aplicación web dentro de la imagen
COPY ./app /app

# Puerto en el que escuchará el contenedor
EXPOSE 5000

CMD python main.py
