import pandas as pd
from sqlalchemy.orm import sessionmaker
from modelo import engine
from modelo import Pais, Serie, Plataforma


Session = sessionmaker(bind=engine)
session = Session()

data = pd.read_csv('../data/series.csv')

for _, row in data.iterrows():
    titulo = row['titulo'].strip()
    genero = row['genero'].strip()
    anio_estreno = int(row['anio_estreno'])
    temporadas = int(row['temporadas'])
    
    # Renombramos estas variables para mayor claridad
    nombre_plataforma = row['plataforma'].strip()
    nombre_pais = row['pais'].strip()
    
    # Buscamos los objetos en la base de datos
    pais_obj = session.query(Pais).filter_by(nombre=nombre_pais).first()
    plataforma_obj = session.query(Plataforma).filter_by(nombre=nombre_plataforma).first()
    
    # Creamos la Serie con los nombres exactos del modelo
    nueva_Serie = Serie(
        titulo = titulo,
        genero = genero,
        anio_estreno = anio_estreno,
        temporadas = temporadas,
        plataforma = plataforma_obj,  
        pais = pais_obj               
    )
    session.add(nueva_Serie)
    
session.commit()
session.close()

print("Los datos se cargaron correctamente")