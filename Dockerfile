# Imagen base
FROM python:3.12-slim

# Establecer directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar requirements primero (mejor para caching)
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del proyecto
COPY . .

# Exponer el puerto donde corre Flask
EXPOSE 5000

# Comando para ejecutar la API
CMD ["python", "conversor.py"]