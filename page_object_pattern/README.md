# Web Scraping con enfoque de Page Object Pattern

Es un patrón de diseño para escribir el código del Web Scraping que sigue el patrón del mundo de las pruebas automatizadas.

Consiste en esconder los queries especificos que se utilizan para manipular un documento HTML detrás de un objeto que representa la página web.

Si estos queries se añaden directamente al código principal, el códigp es bastante frágil. Arreglarlo se vuelve muy díficil. El código se vuelve vulnerable a los cambios que sufrirán las páginas web.

El esqueleto de la estructura del proyecto es el siguiente:
* `config.yaml`: La configuración global de las variables. Contiene mapas con los valores de las páginas a screapear.
* `common.py`: Script para cargar la configuración del proyecto. Cargamos en memoria la configuración del archivo yaml.
* `main.py`: La lógica del scrapeo.

El enfoque se trata que cada página web a scrapear, se le vea y sea tratada como un objeto, abstraerse en una página - objetos.