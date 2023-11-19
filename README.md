# LinkedinBot
LinkedinBot es un script en Python que utiliza Selenium para automatizar la interacción con la plataforma LinkedIn. Su principal función es extraer direcciones de correo electrónico a partir de una lista predefinida de enlaces de perfiles de LinkedIn.

## Requisitos
- Python
- Selenium
- WebDriver para Chrome (ChromeDriver)

## Instalación
1. Asegúrese de tener Python instalado en su sistema.
2. Instale Selenium utilizando el comando: ``pip install selenium``.
3. El script gestionará la instalación de ChromeDriver automáticamente.

## Uso
Para usar el script, siga estos pasos:
1. Clone el repositorio usando ``git clone https://github.com/PlacidoDiaz/LinkedinBot.git``
2. Prepare un archivo **links.txt** conteniendo URLs de perfiles de LinkedIn, uno por línea.
3. Ejecute el script utilizando el siguiente comando en la terminal, donde <correo> y <contraseña> son sus credenciales de inicio de sesión en LinkedIn.

````
python LinkedinBot.py <correo> <contraseña>
````

## Funcionalidades
El bot realiza las siguientes acciones:

1. Inicia sesión en LinkedIn usando las credenciales proporcionadas.
2. Recorre la lista de enlaces proporcionada en links.txt.
3. Visita cada perfil y extrae la dirección de correo electrónico (si está disponible).
4. Almacena todas las direcciones de correo electrónico en un archivo correos.txt.

## Advertencias

1. El uso de este script para extraer información de LinkedIn puede violar los términos de servicio de la plataforma.
2. La eficacia del script depende de las actualizaciones en la interfaz de LinkedIn y podría requerir ajustes con el tiempo.
3. Este script es solo para fines educativos y no debe usarse para recopilar datos sin el consentimiento explícito de los usuarios.
