import pandas as pd
from sqlalchemy.orm import sessionmaker
from modelo import engine
from modelo import Actor, Pais, Serie, Plataforma

Session = sessionmaker(bind=engine)
session = Session()

data1 = pd.read_csv('../data/paises.csv')


for _, row in data1.iterrows():
    nombre = row['nombre'].strip()
    continente = row['continente'].strip()
    
    nuevo_pais = Pais(
        nombre = nombre,
        continente = continente
    )
    session.add(nuevo_pais)
    
session.commit()
session.close()

print("Los datos se cargaron correctamente")