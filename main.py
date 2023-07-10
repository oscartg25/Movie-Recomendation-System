from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel
from typing import Optional

df_union = pd.read_excel('df_union.xlsx')

app = FastAPI()


@app.get("/")
def Index():
    return {"message": "hola, Bienvenidos "}

# Resto de las rutas y funciones relacionadas a las consultas

# Endpoint para obtener la cantidad de películas producidas en un idioma específico y su relación con el año de estreno
@app.get('/peliculas_idioma{idioma}')
def peliculas_idioma(idioma: str):
    filtered_df = df_union[df_union['original_language'] == idioma]
    count = filtered_df.shape[0]
    years = filtered_df['release_year'].tolist()
    return {"idioma": idioma, "cantidad": count, "años_estreno": years}

# Endpoint para obtener la duración y el año de una película específica
@app.get('/peliculas_duracion/{pelicula}')
def peliculas_duracion(pelicula: str):
    peli=df_union[df_union['title']== pelicula].iloc[0]
    duracion=peli['runtime']
    anio=peli['release_year']
    return{'respuesta':f"(pelicula),duracion:{duracion}, Año:{anio}"}
                                                    
    
#

# Endpoint para obtener información de una franquicia específica
@app.get('/franquicia')
def franquicia(Franquicia: str):
    filtered_df = df_union[df_union['franchise'] == Franquicia]
    if filtered_df.empty:
        return {"mensaje": f"No se encontró la franquicia '{Franquicia}'."}
    cantidad_peliculas = filtered_df.shape[0]
    ganancia_total = filtered_df['revenue'].sum()
    ganancia_promedio = filtered_df['revenue'].mean()
    return {"Franquicia": Franquicia, 
            "Cantidad de películas": cantidad_peliculas, 
            "Ganancia total": ganancia_total, 
            "Ganancia promedio": ganancia_promedio}

# Endpoint para obtener la cantidad de películas producidas en un país específico
@app.get('/peliculas_pais/{pais}')
def peliculas_pais(pais: str):
    filtered_df = df_union[df_union['production_countries02'].str.contains(pais, case=False)]
    cantidad_peliculas = filtered_df.shape[0]
    return {"mensaje": f"Se produjeron {cantidad_peliculas} películas en el país {pais}"}

# Endpoint para obtener información de una productora específica
@app.get('/productoras_exitosas/{productora}')
def productoras_exitosas(productora: str):
    df_cleaned = df_union.dropna(subset=['production_companies'])
    filtered_df = df_cleaned[df_cleaned['production_companies'].str.contains(productora, case=False)]
    count = filtered_df.shape[0]
    return {"productora": productora, "cantidad": count}

# Endpoint para obtener información sobre un director específico
@app.get('/get_director')
def get_director(nombre_director: str):
    filtered_df = df_union[df_union['Director'].str.contains(nombre_director, case=False)]
    peliculas = []
    
    for _, row in filtered_df.iterrows():
        pelicula = {
            "nombre": row['title'],
            "fecha_lanzamiento": str(row['release_date']),
            "retorno_individual": row['return'],
            "costo": row['budget'],
            "ganancia": row['revenue']
        }
        peliculas.append(pelicula)
    
    return {"director": nombre_director, "peliculas": peliculas}