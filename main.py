from fastapi import FastAPI
from fastapi.responses import JSONResponse,HTMLResponse
import pandas as pd
import ast


app = FastAPI(title= 'Games-Steam-API')


# Endpoint de la función user_data: Recibe un string con el user_id
# Retorna un resumen del mismo con la cantidad de dinero gastada, 
# los items adquiridos y el porcentaje de juegos recomendados 
@app.get("/userdata/{user_id}",tags=['Funcion User'])
def userdata(user_id : str):
    '''
    **User Data:**Recibe un string con el **"User Id"** y devuelve un summary del user</br>
    
    Ejemplo: --000--

        {
        "user_id": "--000--",
        "porcentaje_recomendacion": 100,
        "cantidad_gastada": 402.77,
        "cantidad_items": 58
        }
    '''
    df_user = pd.read_csv("df-funcion-1.csv")
    user_data = df_user[df_user['user_id'] == user_id]

    if len(user_data) == 0:
        return JSONResponse(status_code=404,content={'error': f"User with id '{user_id}' not found"})

    response = user_data.to_dict(orient='records')
    return JSONResponse(status_code=200,content={"results":response})


# Endpoint de la función countreviews: Recibe dos fechas en formato str
# Retorna la cantidad de usuarios que hicieron reviews entre esas fechas
# y el porcentaje de recommended 
@app.get("/countreviews/{date1}/{date2}", tags=['Funcion Fechas de Reviews'])
def countreviews(date1,date2 : str):
    '''
    **Count Reviews:** Recibe dos **fechas** en formato string y devuelve
    la cantidad de usuarios que realizaron reviews y el porcentaje de recomendación
    entre las fechas dadas. </br>

    Ejemplo: date1: 2011-11-5, date2: 2014-07-8 </br>

        { "results": [
            {
                "cantidad_usuarios": 17072, 
                "porcentaje_recomendacion": 0.91
            }]
        }
    '''
    df_counter = pd.read_csv("df_counter_func_2.csv")
    cantidad_usu_rese = df_counter[(df_counter["Fecha"]>=date1)& (df_counter["Fecha"]<=date2)]["user_id"].nunique()
    recommend = df_counter[(df_counter["Fecha"]>=date1)& (df_counter["Fecha"]<=date2)]["recommend"]
    true_count = recommend.value_counts().get(True, 0)  
    porce_recom = true_count / len(recommend) if len(recommend) > 0 else 0  

    response = {'cantidad_usuarios':cantidad_usu_rese, 'porcentaje_recomendacion':round(porce_recom,2)}
    
    return JSONResponse(status_code=200, content={"results":response})


# Endpoint de la función Género: Se ingresa un genero en formato str
# Devuelve un objeto json con el genero cantidad de horas y rank
# en base de las horas jugadas totales de todos los géneros
@app.get("/genre/{genre}",tags=['Funcion Genre'])
def genre(genre : str):
    '''
    **Genre:** Recibe un string con el nombre del género a evaluar</br>
    Devuelve el rank de las categorías con más horas jugadas por los usuarios</br>
    y su total de horas jugadas.</br><br/>

    Ejemplo: RPG

        {
        "results": [
            {
            "Genre": "rpg",
            "Total_Hours": 1041022718,
            "Rank": 3
            }]
        }

    '''
    genre = genre.lower().strip()
    df_genre = pd.read_csv('df-funcion-3.csv')
    
    if df_genre['Genre'].str.contains(genre).any():
        genre_info = df_genre[df_genre['Genre']==genre]
        response = genre_info.to_dict(orient='records')

    else:
        return JSONResponse(status_code=404,content={'error':f"Genre '{genre}' not found"})

    return JSONResponse(status_code=200,content={"results":response})


# Endpoint de la función user_for_genre: Recibe un string para el genero
# Regresa el top5 de los usuarios con mas horas de juego
@app.get("/userforgenre/{genero}",tags=['Funcion top User x Genre'])
def userforgenre( genero : str ):
    '''
    **User for Genre:** Recibe un string con el género que se desea evaluar</br>
    Devuelve una lista ordenada de los usuarios ("User Id" y "User Url") con más horas jugadas según el ranking de cada género</br></br>

    Ejemplo: Indie

        {
        "results": [
            {
            "user_id": "wolop",
            "user_url": "http://steamcommunity.com/id/wolop"
            },
            {
            "user_id": "76561198039832932",
            "user_url": "http://steamcommunity.com/profiles/76561198039832932"
            },
            {
            "user_id": "tsunamitad",
            "user_url": "http://steamcommunity.com/id/tsunamitad"
            },
            {
            "user_id": "jimmynoe",
            "user_url": "http://steamcommunity.com/id/jimmynoe"
            },
            {
            "user_id": "lildoughnut",
            "user_url": "http://steamcommunity.com/id/lildoughnut"
            }
        ]
        }
    '''
    genero = genero.lower().strip()
    df1 = pd.read_csv('df-funciones-4.csv')

    if genero not in df1.columns:
        return JSONResponse(status_code=404,content={'error':f"Genre '{genero}' not found"})
    
    top5 = df1.sort_values(by=genero,ascending=False).head(5).reset_index()
    response = top5[['user_id','user_url']].to_dict(orient='records')

    return JSONResponse(status_code=200,content={"results":response})


# Endpoint de la función Developer: Recibe un desarrollador
# Devuelve la cantidad total de items y el porcentaje de items gratis por cada año
@app.get("/developer/{developer}", tags=['Items gratis por año segun el Developer'])
def developer(developer : str):
    '''
    **Developer:** Recibe un string con el nombre del desarrollador. 
    Devuelve una lista de cada año donde el desarrollador publicó juegos con su porcentaje de juegos free to play por año

    Ejemplo: Mortis Games

        {
        "results": [
            {
            "release_year": 2017,
            "item_count": 3,
            "porcentaje_free": 33.33
            }
        ]
        }
    '''
    df = pd.read_csv("df-funcion-5.csv")
    developer = developer.strip().lower()

    if df['developer'].str.contains(developer).any():
        data = df[df['developer'] == developer]
        data = data.sort_values('release_year', ascending=False)
        response = data[['release_year','item_count','porcentaje_free']].to_dict(orient='records')
        return JSONResponse(status_code=200, content={"results":response})

    else:
        return JSONResponse(status_code=404, content={'error': f"Developer {developer} not found"})