# Movie-Sistem-Project

Este proyecto va contener un sistema de recomendacion en el cual nos arojara las distintas peliculas recomendadas a partir de diferentes aspectos.

por lo tanto extraemos los datos usando dos dataset: credits.csv y movies_dataset.xls usando el archivo ETL.ipynb en el cual desarrolaremos nuestra ETL.

En primer lugar procedemos a realizar una lectura de los datos df1= pd.read_excel('Dataset/movies_dataset.xlsx') y df2 = pd.read_csv('Dataset/credits.csv'), luego realizamos una limpieza de estos datos para poder obtener unos calculos y analisis en mejor forma.

luego de la limpieza obtenemos una union de las dos dataset, en las cuales pudimos observar muchos datos anidados como en la columna, Belong_to_collection, genres, production_companies, production_countries, siendo estas las que mas utilizaremos ya que al desanidar cada una de estas obtendremos unos valores importantes para nuestro analisis. en Belong_to_collection podremos obtener lo que serian las franquicias de cada pelicula, en production_companies podremos obtener las distintas producciones que participaron en la fimlacion de dicha pelicula, en production_countries al desanidar obtenemos los paises en donde se realizo dicha filmacion, y en genres los distintos generos de estas peliculas.

para ser efectivo un proceso de ETL necesitaremos que estos datos extraidos, en los cuales muchos fueron transformados, debemos guardar estos datos por lo tanto accedimos a exportar los distintos datos de esta ETL utilizando un archivo.xls llamado df_union.xls en el cual guardaremos todos estos datos ya extraidos y transformados. 

FUNCIONES Y CREACION DE API

 Para poder realizar dichas funciones y api debemos importar las distintas librerias que nos van a permitir hacer esto(fastapi, numpy, pandas), por lo cual procedemos a crear 6 funciones en las cuales nos permitiran interactuar con los datos extraidos de los dataset y de esta forma crear una api que nos permita intercambiar distintas busquedas de estas peliculas, estas 6 funciones de las cuelas fueron:

-peliculas_idioma: para obtener la cantidad de películas producidas en un idioma específico 
-peliculas_duracion: para obtener la duración y el año de una película específica
-franquicia: para obtener información de una franquicia específica
-peliculas_pais: para obtener la cantidad de películas producidas en un país específico
-productoras_exitosas:para obtener información de una productora específica
-get_director: para obtener información sobre un director específico

teniendo en cuenta estas distintas funciones se procedio a crear una funcion en la cuel estableceriamos un sistema de recomendacion el cual nos permitiria que por cada pelicula nos recomendara otras 5 teniendo en cuenta sus similitudes, en generos, en puntuacion, entre otros aspectos por lo cual creamos una funcion llamada recomendacion.

para realizar las funciones decidimos usar el archivo main.py con el cual conectaremos por medio de fastapi nuestro local host en el cual podemos interactuar con las api utilizando el comando uvicorn main:app --port 2707, en la cual nos arrojara una direccion ( http://127.0.0.1:2707) donde podemos encontrar nuestra api, y tambien por medio de nuestra interfaz en render. 


