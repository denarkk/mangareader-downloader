# Manga Reader Downloader 1.0

![mrdownloaderexec](http://i.imgur.com/Dxlz2wn.gif)

## Instrucciones en Español

Esta utilería para la línea de comandos te servirá para descargar episodios de cualquier manga que se encuentre en la base de datos de [MangaReader](http://www.mangareader.net) estando éstos obviamente en el idioma **Inglés**. Corre utilizando el intérprete de Python por lo que deberás tener instalado Python en tu computadora así como 2 módulos (*Beautifulsoup4* y *Requests*) necesarios para descargar las imágenes y realizar las peticiones a MangaReader; más adelante se te enseñará a instalar los requerimientos para poder ejecutar esta utilería.

#### 1- Instalar Python
De preferencia *Python 3+*, si ya tienes instalado Python puedes saltarte este paso.

Para instalar la última versión de Python deberás ir a [Python.org](https://www.python.org/downloads/) y luego entrar a la sección de Descargas (downloads), para luego hacer click en el botón de descarga, hoy siendo un 23 de Enero del 2016, la versión más actual de Python es la 3.5 y así luce es botón de descarga desde la **página oficial**:

![pydownload](http://puu.sh/mHsgI/1033540ac1.png)

**IMPORTANTE**: Asegúrate que cuando lo estés por instalar, marques la opción de **"Add Python 3.X to PATH"** ya que de lo contrario tendrás que buscar el directorio de Python en tu computadora y añadirlo a las variables de entorno PATH de [forma manual](https://devcode.la/tutoriales/instalacion-de-python-27-en-windows-8/). Esto es importante para poder ejecutar el intérprete de Python desde cualquier directorio.

![PATH](http://puu.sh/mHso5/f99bd39625.jpg)

Para finalizar presiona **"Install Now"** y cuando termine, continúa al siguiente paso.

#### 2- Instalar los módulos necesarios con PIP

Las versiones de Python 3.4 en adelante tienen integrado por defecto el instalador de paquetes y módulos **"PIP"**, éste es necesario para instalar los módulos **BeautifulSoup4** (Un web-scrapper para Python) y **Requests** (Manejador de peticiones HTTP) de los que *MangaReader Downloader* hará uso para descargar el episodio de Manga.

En caso de que tu versión de Python sea menor a 3.4, para instalar PIP manualmente entra a [este tutorial](https://www.youtube.com/watch?v=zPMr0lEMqpo).

##### 2.1- Instalar BeautifulSoup

Abre la línea de comandos (**Tecla WINDOWS** + **R** y escribir **CMD**, luego **ENTER**).

Escribe `pip install beautifulsoup4` y presiona ENTER para enviar el comando. Deberás ver algo así:

![bs4](http://puu.sh/mHtfN/5c5c9258be.jpg)

##### 2.2- Instalar Requests

En la misma ventana de la línea de comandos (consola o terminal, como le quieras llamar), escribe `pip install requests` y presiona ENTER, cuando termine de instalar deberás ver algo así:

![req](http://puu.sh/mHtiO/2ca2f803df.jpg)

#### 3- Descargar el script MangaReader Downloader 1.0

Ya tienes todo lo necesario para ejecutar el script, descarga [este archivo RAR](https://github.com/luishendrix92/mangareader-downloader/releases/download/v1.0/mangareader-downloader-1-0.rar) y **extrae** los 2 archivos (*manga.py* y *helpers.py*) en la carpeta **C:/Users/tu_usuario** en donde *tu_usuario* representa el nombre de tu computadora o de usuario en Windows, para ubicarte mira este ejemplo:

![cmddir](http://puu.sh/mHtyh/71c3f1d1b3.png)

> **NOTA**: Dado que el script lo vas a ejecutar desde la línea de comandos (trata de memorizar la forma de abrirla, Windows + R y escribiendo CMD), asegúrate que la línea de comandos empiece en el directorio de tu usuario en Windows, si no, mete los 2 archivos *.py* en el directorio que indique la línea de comandos al abrirse.

#### 4- Utilizar MangaReader Downloader 1.0

Llegamos a lo divertido, usar la utilería! Es fácil, lo único que tienes que hacer es abrir la línea de comandos (ya lo sabes hacer) y escribir `python manga.py [nombre del manga] [numero del episodio]` en donde [nombre del manga] es el nombre del manga del que quieras descargar un episodio, asegurándote de que si el nombre contiene espacios, ponerlo entre comillas. El [número del episodio] es simplemente el número del capítulo del manga que quieras descargar (se descargarán las páginas de éste).

**Ejemplos**: `python manga.py naruto 700`, `python manga.py "school rumble" 15` o la imagen que viste al principio.

En caso de que el episodio aún no haya sido lanzado o no exista, saldrá un mensaje en la consola. Si el nombre del manga es incorrecto, el programa terminará de ejecutarse sin avisar nada (lo estoy corrigiendo para la siguiente versión).

Tu episodio se descargará por defecto en la carpeta **C:/Manga** en el directorio **/nombre del manga/numero de epsiodio**.

> **Nota**: En futuras versiones se podrá cambiar esto desde la interfaz de usuario que estoy creando pero si quieres cambiarla ahora, tendrás que editar el archivo *manga.py* y cambiar la variable *globalpath* a una que sea de tu agrado. Si eres usuario de Mac OS X puedes probar con un directorio absoluto pero no garantizo su funcionamiento, no pensé este programa para usuarios de Mac.

## English Instructions

Coming soon, the Spanish speaking community has a high priority.

# Future Possible Additions

- More manga providers, in both Spanish and English (Submanga, MangaFox, MangaPanda, etc).
- The capability of downloading a range of episodes and not just 1.
- An installer to make it easier for users not having to install Python and the required modules.
- A user interface for a better user experience.
