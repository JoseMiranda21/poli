# imagen
FROM python:3.6.9

# Instalar las dependencias necesarias
# RUN apk update && apk add --no-cache bash

# Copiar los archivos de la aplicación al contenedor
COPY app1.py /app1.py

# Establecer permisos de ejecución
RUN chmod +x /app1.py

# Ejecutar el script de la aplicación
CMD ["python", "/app1.py"]