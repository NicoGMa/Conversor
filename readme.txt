Este proyecto forma parte de mi proceso de aprendizaje en DevOps.
Consiste en una API de conversión de monedas construida en Python (Flask), completamente dockerizada y acompañada por un pipeline CI/CD implementado con GitHub Actions.

Tecnologías utilizadas
Python 3 / Flask
Docker
Docker Hub
GitHub Actions (CI/CD)
AWS EC2 (Ubuntu)
SSH + Secrets Management

El objetivo principal es demostrar conocimientos prácticos sobre:

Construcción y despliegue de aplicaciones con Docker

Automatización mediante GitHub Actions

Gestión de secrets y seguridad

Preparación de infraestructura para deploy en AWS

Flujo completo CI/CD aplicado a un caso real



Funcionalidades principales

✔️ API en Flask

Endpoint para conversión de monedas

Manejo de solicitudes y parámetros

Estructura de un servicio real


✔️ Dockerización completa

Dockerfile optimizado

Imagen construida localmente y en CI

Publicación automática en Docker Hub


✔️ CI – Integración Continua

Pipeline CI realizado con GitHub Actions:

Clona el repositorio

Loguea en Docker Hub usando secrets

Construye la imagen usando el commit SHA

Publica automáticamente en Docker Hub

Actualiza también la etiqueta latest

Demuestra conocimientos en:

Automatización de builds

Manejo de variables/secretos



✔️ CD – Despliegue Continuo (en progreso)

El proyecto actualmente incluye:

EC2 configurada para recibir despliegues

Conexión SSH desde GitHub Actions correctamente configurada

Workflow CD preparado

Validación de acceso y permisos

Infraestructura lista para ejecutar deploy.sh


Próximo paso:
Agregar el archivo deploy.sh en la instancia EC2 que actualiza el contenedor y reinicia el servicio automáticamente.


