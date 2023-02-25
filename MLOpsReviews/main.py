from fastapi import FastAPI
import pandas as pd
#from pandasql import sqldf
import os
os.environ["OPENBLAS_L2SIZE"]="512k"

app = FastAPI()

@app.get("/")
def presentacion():
    return "Proyecto Individual 01 - Monse castillo!"

@app.get("/contacto")
def contacto():
    return "Email: monsegomcas@gmail.com / Github: BeeluRiddle"

@app.get("/menu")
def menu():
    return ("Funciones: (1) get_word_count (2) get_score_count (3) get_second_score (4) get_longest (5) get_rating_count ")

#----------QUERIES----------
#Consigna 1: Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma
@app.get("/get_max_duration/{platform}/{anio}/{tipo}")
def get_max_duration(platform = None, anio = None, tipo = None):
    #Lectura de la base de datos:
    print('platform, Año, tipo')
    df = pd.read_csv("movie_set.csv")

    #Definición de las plataformas:
    if platform == "amazon":
        plat = "a"
    elif platform == "disney":
        plat = "d"
    elif platform == "hulu":
        plat = "h"
    elif platform == "netflix":
        plat = "n"
    else:
        pass
    
    if (platform != None and anio != None and tipo != None):
        df_filtro = df[df['id'].str.contains(plat, regex=True, na=True)]
        df_filtro = df_filtro[(df_filtro['release_year'] == anio) &  (df_filtro['duration_type'] == tipo)]
        print('0')
    elif(platform != None and anio != None and tipo == None):
        df_filtro = df[df['id'].str.contains(plat, regex=True, na=True)]
        df_filtro = df_filtro[(df_filtro['release_year'] == anio)]
        print('1')
    elif(platform != None and anio == None and tipo != None):
        df_filtro = df[df['id'].str.contains(plat, regex=True, na=True)]
        df_filtro = df_filtro[(df_filtro['duration_type'] == tipo)]
        print('2')
    elif (platform == None and anio != None and tipo != None):
        df_filtro = df[(df['release_year'] == anio) &  (df['duration_type'] == tipo)]
        print('3')
    elif (platform == None and anio != None and tipo == None):
        df_filtro = df[(df['release_year'] == anio)]
        print('4')
    elif (platform == None and anio == None and tipo != None):
        df_filtro = df[(df['duration_type'] == tipo)]
        print('5')    
    else: df_filtro = df 
    maximo = df_filtro['duration_int'].max()
    return maximo

