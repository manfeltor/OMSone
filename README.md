# proyectofinal_torres_jimenez_manuel

# OMSone v0.1

## Descripción del Proyecto

Nuestro proyecto, **OMSone**, apunta a ser un sistema de gestión de pedidos robusto pero fácil de usar. Está diseñado para optimizar las operaciones logísticas y simplificar el procesamiento de pedidos para empresas de todos los tamaños. Construido sobre tecnologías web modernas, nuestro sistema proporcionará soluciones innovadoras para los desafíos comunes en el ámbito de la logística.

## Características Clave

- **Gestión de Compañías:** Crea y gestiona compañías para segmentar órdenes de proveedores y clientes.
- **Registro de Empleados:** Asigna roles y permisos específicos a empleados para un control granular.(en construccion)
- **Personalización de Usuarios:** Permite personalizar avatares y datos de usuarios por roles y compañías.(roles en construccion)
- **Carga y Modificación Masiva de Órdenes:** Importa y modifica órdenes fácilmente desde archivos de Excel.(en construccion)
- **Clasificación Automática de Órdenes:** Utiliza un algoritmo para interpretar datos y mejorar la planificación.(en construccion)
- **RESTful APIs:** Integración sencilla con aplicaciones externas para actualizaciones en tiempo real.(en construccion)
- **Seguimiento en Tiempo Real:** Proporciona a los clientes seguimiento en tiempo real de sus órdenes.(en construccion)
- **Análisis de Negocios:** Genera informes personalizados para análisis profundo y proyecciones.(en construccion)

## Stack Tecnológico

- **Backend Framework:** Django (Python)
- **Base de Datos:** PostgreSQL (SQL lite como estándar)
- **APIs:** Django REST Framework
- **Frontend:** HTML, CSS, JavaScript
- **Despliegue:** Docker, AWS
- **Control de Versiones:** Git, GitHub

## motor

**engine:**
  ```bash
  python==3.11
  ```
## dependencias

**lib:**
```bash
  absl-py==2.0.0
asgiref==3.7.2
astunparse==1.6.3
cachetools==5.3.1
certifi==2023.7.22
charset-normalizer==3.3.0
click==8.1.7
colorama==0.4.6
contourpy==1.1.1
cycler==0.12.1
distlib==0.3.7
Django==4.2.4
filelock==3.12.3
flatbuffers==23.5.26
fonttools==4.43.1
gast==0.5.4
google-auth==2.23.2
google-auth-oauthlib==1.0.0
google-pasta==0.2.0
grpcio==1.59.0
h5py==3.10.0
idna==3.4
joblib==1.3.2
keras==2.14.0
kiwisolver==1.4.5
libclang==16.0.6
Markdown==3.5
MarkupSafe==2.1.3
matplotlib==3.8.0
ml-dtypes==0.2.0
nltk==3.8.1
numpy==1.25.2
oauthlib==3.2.2
opt-einsum==3.3.0
packaging==23.2
pandas==2.1.0
Pillow==10.0.1
pipenv==2023.9.1
platformdirs==3.10.0
protobuf==4.24.4
pyasn1==0.5.0
pyasn1-modules==0.3.0
pyparsing==3.1.1
python-dateutil==2.8.2
pytz==2023.3
regex==2023.8.8
requests==2.31.0
requests-oauthlib==1.3.1
rsa==4.9
seaborn==0.13.0
sqlparse==0.4.4
termcolor==2.3.0
tqdm==4.66.1
typing_extensions==4.8.0
tzdata==2023.3
urllib3==2.0.6
virtualenv==20.24.4
Werkzeug==3.0.0
wrapt==1.14.1
```
## Instalación en Local

**Para poner en marcha la aplicación, sigue los siguientes pasos:**

1. **Clonar el Repositorio:**
   ```bash
   git clone https://github.com/manfeltor/proyectofinal_torres_jimenez_manuel.git
   cd P1
   
2. **instalar dependencias:**

puedes instalar de forma manual cada una de las dependencias del listado de requerimientos con el comando pip:
  ```bash
  pip install <dependencia>
  ```
o directamente instalar desde el archivo "requeriments.txt":
  pip install -r requirements.txt

3. **configura PostgreSQL database en 'settings.py' o trabaja estandar con SQL lite:**

4. **Corre el servidor de desarrollo:**
  ```bash
  python manage.py runserver
  ```
6. **acceso a la aplicacion:**

en navegador...
```bash
  "http://localhost:8000"
```
## pautas de contribución:

Este pretende ser un proyecto abierto y gratuito en su version predeterminada, pensado para aportar herramienta, acercar tecnologia y generar oportunidades a todos aquellos a quienes pueda generar un valor agregado, pensado principalmente para PYMEs.

Recibimos con brazos abiertos colaboradores de toda la comunidad. para recibir mas pautas sobre la colaboracion en este proyecto contactame a manfeltor@live.com

## Licencia

Este proyecto aun no cuenta con una licencia definida


