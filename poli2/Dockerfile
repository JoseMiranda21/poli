# imagen
FROM python:3.6.9

# Instalar las dependencias necesarias
# RUN apk update && apk add --no-cache bash

# Copiar los archivos de la aplicación al contenedor
COPY app2.py /app2.py

# Establecer permisos de ejecución
RUN chmod +x /app2.py

# Ejecutar el script de la aplicación
CMD ["python", "/app2.py"]
