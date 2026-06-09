# """
# el titulo de la serie con el promedio de edad de los actores que participan en la serie
# """

from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from modelo import Serie, engine

Session = sessionmaker(bind=engine)
session = Session()

# resultados = session.query(
#     Serie.titulo, func.avg(Actor.edad)).join(Actor).group_by(Serie.titulo).all()

# for titulo, promedio in resultados:
#     if promedio is not None:
#         print(f"{titulo}: {promedio:.2f}")

# session.close()

series = session.query(Serie).all()

for serie in series:
    print(f"{serie.titulo} ||||| Edad promedio: {serie.obtener_edad_actores():.2f} ||||| Premios: {serie.obtener_premios()}")

session.close()