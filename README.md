<p align=center><img src=https://raw.githubusercontent.com/bere44/Proyecto_Individual_1/master/src/header_ctms_juegos.jpg><p>

# Proyecto Individual Henry - Recomendación de videojuegos

_Este proyecto es parte de la evaluación de conocimientos del bootcamp de Henry y tiene como objetivo aplicar los conceptos y habilidades adquiridas durante el curso. El proyecto se centra en el análisis de datos, ingeniería de datos y creación de modelos de aprendizaje automático._

## Estructura del Repositorio 🚀


-   **.gitignore**: Archivo que especifica los archivos y directorios que deben ser ignorados por Git.

-   **ETL**: Archivo en donde ser hace la carga de datos y algunas transformaciones.

-   **Nlp.ipynb**: Archivo Python que implementa análisis de sentimientos utilizando NLTK.

-   **Funciones**: Archivo Jupyter Notebook que muestra las funciones a los endpoints del proyecto.

-   **EDA.ipynb**: Archivo Jupyter Notebook que contiene el análisis exploratorio de datos.

-   **Ml.ipynb**: Archivo Jupyter Notebook que contiene la creación y evaluación del modelo de          aprendizaje automático.

-   **Archivos csv**: Son los archivos donde estan los dataset reducidos para usar las diferentes funciones que hay en los archivos de jupiter notebooks.

-   **src**: Carpeta que contiene archivos fuente del proyecto.

-   **Main.py**: Archivo principal del proyecto, este archivo se usa para correr el Api.

-   **Requirements.txt**: Archivo que especifica las dependencias y librerías necesarias para ejecutar el proyecto.

## Etapas del Proyecto 📖

El proyecto se divide en las siguientes etapas:

1. **Extracción de datos**: Se realizaron procesos para limpiar y transformar los datos proporcionados en las bases de datos.

2. **Análisis de Sentimientos**: Se utilizó un archivo que contenía los títulos y etiquetas de los videojuegos para realizar un análisis de sentimientos y determinar la polaridad de las opiniones.

3. **Funciones de consultas**: Se implementaron varias funciones para consultar información específica de los datos:

   - `userdata(User_id: str)`: Devuelve la cantidad de dinero gastado por el usuario, el porcentaje de recomendación en base a las reviews y la cantidad de items.
   - `countreviews(YYYY-MM-DD y YYYY-MM-DD: str)`: Devuelve la cantidad de usuarios que realizaron reviews entre las fechas dadas y el porcentaje de recomendación de los mismos.
   - `genre(género: str)`: Devuelve el puesto en el que se encuentra un género en el ranking de PlayTimeForever.
   - `userforgenre(género: str)`: Devuelve el top 5 de usuarios con más horas de juego en el género dado, junto con su URL y ID de usuario.
   - `developer(desarrollador: str)`: Devuelve la cantidad de items y el porcentaje de contenido gratuito por año según la empresa desarrolladora.

4. **API**: Se implementó una API utilizando FastApi para exponer las funciones de consulta como endpoints y tambien se uso Remder. La documentación de la API se puede encontrar en [https://proyecto-individual-1-bere.onrender.com/docs](https://proyecto-individual-1-bere.onrender.com/docs).

5. **EDA**: Se realizó un Análisis Exploratorio de Datos para obtener información adicional sobre los datos de videojuegos.

6. **Modelo de Machine Learning**: Se desarrolló un modelo de k-vecinos para recomendar 5 juegos utilizando un ID de juego.


## Explicación del proyecto 📸

Puede ver el video con la aplicacion del deployment en render en este enlace(https://drive.google.com/file/d/1IVym2xbm6iaelyxWkf9Q-QiABmWnB5lB/view?usp=drive_link)

## Instrucciones de Uso 📋

1.  Clona el repositorio en tu máquina local:

git clone https://github.com/bere44/Proyecto_Individual_1.git

2.  Instala las dependencias necesarias:

pip install -r requirements.txt

3.  Sigue las instrucciones en cada uno de los archivos Jupyter Notebook para ejecutar y explorar el proyecto.



## Autora ✒️
* **Berenisse de la Cruz**  - [bere44](https://github.com/bere44/)
