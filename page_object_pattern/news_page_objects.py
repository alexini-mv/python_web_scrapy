# Abstracción de nuestros objetos que representaran las páginas web
from unittest import result
import requests
from bs4 import BeautifulSoup

from common import config


class NewsPage:
    """Clase padre para abstraer la configuración de cada página"""

    def __init__(self, news_site_name, url):
        # Cargamos la correspondiente configuración y queries especificos
        self._config = config()['news_sites'][news_site_name]
        self._queries = self._config['queries']
        self._html = self._visit(url)

    def _visit(self, url):
        """Realizamos la petición y parseo de la página principal"""
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:105.0) Gecko/20100101 Firefox/105.0'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status

        return BeautifulSoup(response.text, 'html.parser')

    def _select(self, query_string):
        """Selecciona las etiquetas CSS del query_string a partir del parseo del html"""
        return self._html.select(query_string)


class HomePage(NewsPage):
    """Clase que nos representara a nuestra página web principal de interes"""

    def __init__(self, news_site_name, url):
        super().__init__(news_site_name, url)

    @property
    def article_links(self):
        """Busca los links a partir del query hecho sobre el html. El decorador property
        hace que el método sea invocado como si fuera un atributo de clase. Y es computado
        cada vez que se llama. No puede ser modificado externamente."""
        link_list = []
        for link in self._select(self._queries['homepage_article_links']):
            if link and link.has_attr('href'):
                link_list.append(link['href'])

        return set(link_list)


class ArticlePage(NewsPage):

    def __init__(self, news_site_name, url):
        super().__init__(news_site_name, url)

    @property
    def title(self):
        result = self._select(self._queries['article_title'])
        # Validamos que al menos si nos traiga un resultado
        return result[0].text if len(result) else ''

    @property
    def body(self):
        result = self._select(self._queries['article_body'])
        # Validamos que al menos si nos traiga un resultado
        return result[0].text if len(result) else ''
