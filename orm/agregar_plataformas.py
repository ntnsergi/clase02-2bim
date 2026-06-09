import pandas as pd
from sqlalchemy.orm import sessionmaker
from modelo import Pais, Plataforma, engine

Session = sessionmaker(bind=engine)
session = Session()

data = pd.read_csv('../data/plataformas.csv')

for _, row in data.iterrows():
    nombre = row['nombre'].strip()
    subs = float(row['suscriptores_millones'])
    nombre_pais = row['pais'].strip() 

    pais_obj = session.query(Pais).filter_by(nombre=nombre_pais).first()
    

    nueva_Plataforma = Plataforma(
        nombre = nombre,
        suscriptores_millones = subs,
        pais = pais_obj  
    )
    session.add(nueva_Plataforma)
    
session.commit()
session.close()

print("Los datos se cargaron correctamente")