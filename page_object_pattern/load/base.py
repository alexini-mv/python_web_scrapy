# Utilización del ORM de SQLAlchemy para guardar datos en DB
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Abrimos una conexión a la base de datos
engine = create_engine('sqlite:///newspaper.db')
# Iniciamos una sesión
Session = sessionmaker(bind=engine)
# Declaramos el objeto que construira el schema
Base = declarative_base()