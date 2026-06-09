import pandas as pd
from sqlalchemy.orm import sessionmaker
from modelo import engine
from modelo import Premio, Serie

Session = sessionmaker(bind=engine)
session = Session()

data = pd.read_csv('../data/premios.csv')

for _, row in data.iterrows():
    nombre_premio = row['nombre_premio'].strip()
    categoria = row['categoria'].strip()
    anio = int(row['anio'])
    nombre_serie = row['serie'].strip() # Cambiado para mayor claridad
    
    # Buscamos la serie correspondiente en la base de datos
    serie_obj = session.query(Serie).filter_by(titulo=nombre_serie).first() 
    
    # Creamos el Premio con el argumento correcto según el modelo
    nuevo_Premio = Premio(
        nombre_premio = nombre_premio,
        categoria = categoria,
        anio = anio,
        serie = serie_obj # <--- Corrección aquí
    )
    session.add(nuevo_Premio)
    
session.commit()
session.close()

print("Los datos se cargaron correctamente")