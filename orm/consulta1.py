# """
# el titulo de la serie con el promedio de edad de los actores que participan en la serie
# """

from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from modelo import Serie, Actor, engine

Session = sessionmaker(bind=engine)
session = Session()

resultados = session.query(
    Serie.titulo, func.avg(Actor.edad)).join(Actor).group_by(Serie.titulo).all()

for titulo, promedio in resultados:
    if promedio is not None:
        print(f"{titulo}: {promedio:.2f}")

session.close()