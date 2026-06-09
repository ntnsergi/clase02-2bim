import pandas as pd
from sqlalchemy.orm import sessionmaker
from modelo import engine
from modelo import Actor, Pais, Serie

Session = sessionmaker(bind=engine)
session = Session()

data1 = pd.read_csv('../data/actores.csv')

for _, row in data1.iterrows():
    nombre = row['nombre'].strip()
    edad = int(row['edad'])
    nombre_pais = row['pais'].strip()
    nombre_serie = row['serie'].strip() 
    

    pais_obj = session.query(Pais).filter_by(nombre=nombre_pais).first()
    serie_obj = session.query(Serie).filter_by(titulo=nombre_serie).first() 
    

    nuevo_actor = Actor(
        nombre = nombre,   
        edad = edad,
        pais = pais_obj,   
        serie = serie_obj  
    )
    
    session.add(nuevo_actor)
    
session.commit()
session.close()

print("Los datos se cargaron correctamente")