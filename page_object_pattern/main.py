from asyncore import write
import csv
import datetime
import re
# Hacemos un CLI sencillo con argparse
import argparse
# Libreria para hacer Logs
import logging
from requests import HTTPError
from urllib3.exceptions import MaxRetryError

import news_page_objects as news
from common import config

logging.basicConfig(level=logging.INFO)
# Importamos las función que carga las variables


# Inicializamos el logger
logger = logging.getLogger(__name__)

# Expresiones regulares para checar los links
is_well_formed_link = re.compile(r'^https?://.+/.+$')
is_root_path = re.compile(r'^/.+$')


def _new_scraper(new_site_name):
    """Scrapeamos el sitio elegido"""
    host = config()['news_sites'][new_site_name]["url"]
    logger.info(f"Beginning scraper for: {host}")

    homepage = news.HomePage(new_site_name, host)

    articles = []
    # Por cada link, validamos que esté bien formado y extraemos info
    for link in homepage.article_links:
        article = _fetch_article(new_site_name, host, link)

        if article:
            logger.info("Article fetched!!!")
            articles.append(article)

    _save_articles(new_site_name, articles)

def _save_articles(new_site_name, articles):
    now = datetime.datetime.now().strftime('%Y_%m_%d')
    out_file_name = f"{new_site_name}_{now}_article.csv"

    # Enlistamos en automatico el nombre de columna todas las propiedades que 
    # definimos en los objetos Articulos.
    csv_headers = list(
        filter(
            lambda property: not property.startswith('_'), dir(articles[0])
        )
    )

    with open(out_file_name, 'w+') as f:
        writer = csv.writer(f)
        writer.writerow(csv_headers)

        for article in articles:
            row = [str(getattr(article, prop)) for prop in csv_headers]
            writer.writerow(row)



def _fetch_article(news_site_name, host, link):
    logger.info(f'Start fetching article at {link}')

    article = None
    # Instanciamos el ArticlePage
    try:
        article = news.ArticlePage(news_site_name, _build_link(host, link))
    except (HTTPError, MaxRetryError):
        logger.warning('Error while fechting the article', exc_info=False)

    if article and not article.body:
        logger.warning('Invalide article. There is no body.')
        return None

    return article


def _build_link(host, link):
    """Nos aseguramos que los link obtenidos estén bien formados para
    realizar las peticiones posteriores."""

    if is_well_formed_link.match(link):
        return link
    elif is_root_path.match(link):
        return f"{host}{link}"
    else:
        return f"{host}/{link}"


if __name__ == "__main__":
    # Inicializamos el parsero los argumentos que fueron escritos durante
    # la ejecución del script
    parser = argparse.ArgumentParser()
    # Seteamos una lista con los sitios opcionales que se puede scrapear
    news_site_choices = list(config()['news_sites'].keys())

    # Agregamos un paramétro valido que recibirá el sitio a scrapear
    parser.add_argument("news_site",
                        help="The news site that you want to scrape",
                        type=str,
                        choices=news_site_choices)

    # Capturamos los valores que fueron pasados al parser.
    args = parser.parse_args()

    _new_scraper(args.news_site)
