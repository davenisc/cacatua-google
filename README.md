# cacatua-google
Bot telegram para convertir texto a voz humana con python3 y google, por favor sigue todos los pasos para que el bot funcione bien, este bot ha sido creado por David Vega Zarate, @davenisc en todas las redes sociales.

1. Primero descarga el proyecto completo.
2. Descomprimelo
3. Registrate en Google para usar sus servicios:

Para utilizar el servicio de Text-to-Speech de Google Cloud, debes crear las credenciales para una cuenta de servicio, no para un usuario. Por lo tanto, debes elegir la opción de "Datos de la aplicación" al crear las credenciales.

La opción de "Datos de usuario" se utiliza para crear credenciales para autenticar a los usuarios de una aplicación. Este tipo de credenciales no se pueden utilizar para acceder a los servicios de Google Cloud.

Para crear las credenciales de una cuenta de servicio en Google Cloud, sigue estos pasos:

Accede a la Consola de Google Cloud en https://console.cloud.google.com.
Selecciona el proyecto en el que quieras crear la cuenta de servicio o crea un proyecto nuevo.
En la barra de navegación de la izquierda, haz clic en "IAM y administración".
Haz clic en "Cuentas de servicio".
Haz clic en "Crear cuenta de servicio".
Especifica un nombre y una descripción para la cuenta de servicio y haz clic en "Crear".
Haz clic en "Crear clave".
Selecciona el tipo de clave "JSON" y haz clic en "Crear". Esto descargará un archivo JSON que contiene las credenciales de la cuenta de servicio.
Asegúrate de guardar este archivo JSON en un lugar seguro y de especificar su ubicación correcta en la variable de entorno GOOGLE_APPLICATION_CREDENTIALS.

4. crea un bot con BotFather en telegram para poder obtener un API KEY, esta informacion la debes reemplazar en el archivo app.py
5. corre el siguiente comando si usas linux en la terminal: export GOOGLE_APPLICATION_CREDENTIALS="/home/usuario/Documentos/Cacatua/googlekey/tu-archivo-b64ab2333328.json"
si no usas linux y usas windows usa este comando:

CMD
set GOOGLE_APPLICATION_CREDENTIALS=D:\Documentos_laptop\PROYECTOS\CACATUA\cacatua-google-main\cacatua-google-main\googlekey\client_secret.json

PowerShell
$env:GOOGLE_APPLICATION_CREDENTIALS="D:\Documentos_laptop\PROYECTOS\CACATUA\cacatua-google-main\cacatua-google-main\googlekey\client_secret.json"

7. debes tener instalado Python en tu pc, para instalarlo ve a  https://www.python.org/ y descargalo
8. instala el archivo requirements.txt para tener todas las librerias necesarias para usar el bot.

con estos pasos ya deberias poder usar el bot y generar tus propios audios con inteligencia artificial.

si tienes dudas puedes seguirme en Tiktok como @davenisc y preguntarme sobre su uso

