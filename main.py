from fastapi import FastAPI
from fastapi.responses import JSONResponse,HTMLResponse
import pandas as pd
import ast
from fastapi.staticfiles import StaticFiles


app = FastAPI(title= 'Games-Steam-API')



# ROOT DE LA WEB
@app.get("/")
def read_root():
    '''
    Root de la api donde debe regresar una pagina html
      Con la descripción de como usar los endpoints
    '''
    with open("index.html", "r", encoding="utf-8") as file:
        response = file.read()
    
    return HTMLResponse(status_code=200,content=response)


# Endpoint de la función user_data: Recibe un string con el user_id
# Retorna un resumen del mismo con la cantidad de dinero gastada, 
# los items adquiridos y el porcentaje de juegos recomendados 
@app.get("/userdata/{user_id}",tags=['User'])
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
    df_user = pd.read_csv('df-funcion-1-1.csv')
    user_data = df_user[df_user['user_id'] == user_id]

    if len(user_data) == 0:
        return JSONResponse(status_code=404,content={'error': f"User with id '{user_id}' not found"})

    response = user_data.to_dict(orient='records')
    return JSONResponse(status_code=200,content={"results":response})


# Endpoint de la función countreviews: Recibe dos fechas en formato str
# Retorna la cantidad de usuarios que hicieron reviews entre esas fechas
# y el porcentaje de recommended 
@app.get("/countreviews/{date1}/{date2}", tags=['Reviews'])
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