# Web Scraping con enfoque de Page Object Pattern

Es un patrón de diseño para escribir el código del Web Scraping que sigue el patrón del mundo de las pruebas automatizadas.

Consiste en esconder los queries especificos que se utilizan para manipular un documento HTML detrás de un objeto que representa la página web.

Si estos queries se añaden directamente al código principal, el códigp es bastante frágil. Arreglarlo se vuelve muy díficil. El código se vuelve vulnerable a los cambios que sufrirán las páginas web.

El esqueleto de la estructura del proyecto es el siguiente:
* `config.yaml`: La configuración global de las variables. Contiene mapas con los valores de las páginas a screapear.
* `common.py`: Script para cargar la configuración del proyecto. Cargamos en memoria la configuración del archivo yaml.
* `main.py`: La lógica del scrapeo.

El enfoque se trata que cada página web a scrapear, se vea y sea tratada como un objeto, abstraerse en una página - objetos.

En el archivo `news_page_objects.py` tiene la definición de las clases que definirán los Page Objects. Cada clase representará a las páginas que serán scrapeadas.

En primer lugar, tenemos una *superclase* `NewsPage` que contendrá la carga de la configuración de cada página a partir de la función config. Definirá los métodos para solicitar el correspondiente request y el método para seleccionar el elemento a partir de los selectores en el config.

Después, como clases hijas, heredando de  `NewsPage`, se definen las correspondientes a cada página, por ejemplo, el `HomePage` y los `ArticlePage`. Aquí se definen los métodos para obtener la información requerida, uno método por elemento buscado. Se le agrega el decorador built-in `@property`, que hace que el resultado regresado por el método sea tratado como atributo. Además, cada vez que se llame el *atributo*, será calculado (ya que en el fondo es realmente un método).

Así, por ejemplo, en la clase `HomePage`, solo tenemos el *atributo* que trae la lista de links de los artículos desplegados en la página principal.

En cambio en la clase `ArticlePage`, tenemos dos *atributos*. El primero trae o busca el título del artículo, mientras que en el segundo regresa el cuerpo del artículo noticioso.

Finalmente en el archivo `main.py` se incluye la lógica y los for-loops para instanciar cada página con su objeto `HomePage` o `ArticlePage`. Una vez obtenido la información, se guarda en un csv, para su posterior limpieza y guardado.