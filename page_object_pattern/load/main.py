import argparse
import logging
logging.basicConfig(level=logging.INFO)

import pandas as pd

from base import Base, engine, Session
from article import Article

logger = logging.getLogger(__name__)

def main(filename):
    # Genera el schema de la DB
    Base.metadata.create_all(engine)
    # Abrimos sesión
    session = Session()
    # Cargamos los datos del csv a memoria
    articles = pd.read_csv(filename)

    for index, row in articles.iterrows()
        # Agregamos fila por fila cada uno de los articulos al schema
        logger.info(f'Loading article uid {row["uid"]}')
        article = Article(row['uid'],
                        row['body'],
                        row['host'],
                        row['newspaper_uid'],
                        row['n_tokens_body'],
                        row['n_tokens_title'],
                        row['title'],
                        row['url'])

        session.add(article)

    # Guardamos en la DB y cerramos
    session.commit()
    session.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='The file you want to load into the db', type=str)

    args = parser.parse_args()

    main(args.filename)