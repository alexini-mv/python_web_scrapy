# Python Web Scrapy
Tutoriales y ejemplos para realizar web scrapeos simples en python

* Web scrapy con Python y XPath en:
    * 01-web_scrapy_xpath.ipynb

## Web Scrapy con XPath y Python

**XPath** es una técnica para extraer datos a partir de objetos **HTML**. 

    XPath es a HTML lo que es Expresiones Regulares a Texto simple.
    
En todas las páginas web tiene un archivo llamado robots.txt que contiene las directrices para que permitir o no permitir los sitios que se pueden realizar web scraping. Por ejemplo:

```
User-agent: *
Allow: /
Disallow: /etc/

Sitemap: https://www.algo.com/sitemap.xml
```

XPath toma cada etiqueta del html como un nodo, con orden jerárquico. Así, XPath nos permite movernos entre nodos para llegar a la información que queremos consultar.

### Síntaxis

La síntaxis de XPath es la siguiente:

+ **/** : Explorar sobre la raíz del documentos o cambiar al siguiente nivel de nodo.
+ **//** : Salta entre todos los niveles de nodas para explorar.
+ //h1 : Salta entre nodos y encuentra todas la etiquetas h1.
+ text() : Trae el texto que contiene la etiqueta que te antecede.
+ /.. : Salta al nodo padre de donde te encuentras.
+ @*atributo* : Para extraer atributos dentro de los nodos.

### Predicados
Para filtrar mejor los elementos que queremos localizar, usamos *predicados* con la siguiente síntaxis: [*predicado*]. Algunos predicados básicos utiles son:

+ **n** : Hace referencia al n-esimo elemento que encuentra, iniciando desde 1.
+ last() : Hace referencia al último elemento.
+ @*atributo* : Trae todos los nodos que contienen a ese atributo.
+ @atributo="algo" : Trae todos nodos que tienen el valor *algo* en el atributo.

Ejemplo en el navegador (JavaScript):
```
$x('//span[@class="text"]/text()')
```

### Operadores Lógicos
Tambien existen operadores lógicos que se pueden usar junto con los predicados:
+ !=
+ =
+ <, >, <=, >=
+ and
+ or
+ not
+ position()

Ejemplos:
```
'//span[@class!="text"]'
'//div[position()>5]'
'//span[@class="text" or @class="tag-item"]'
'//span[not(@class)]'
```

### Wildcards o Comódines
Tambien tenemos Wildcards o Comódines, que son simbolos para traer objetos que no tenemos claro como se llaman.
+ /* : Astérisco indica que traiga todos los nodos inmediatamente después del de la expresión.
+ @* : Trae todos los atributos de todos los nodos.
+ /node() : Trae todo el contenido del nodo, incluyendo nodos o texto.

### Funciones In-text
Tambien podemos realizar una busqueda de patrones directamente dentro del texto que contene los nodos. (In-text). Esto se realiza usando funciones denro de la sección del predicado:
+ [stats-with(., "L")] : Realiza una busqueda con coincidencias de textos que empiezan con la letra L.
+ [contains(., "g")] : Realiza busqueda de coincidencias que incluyen en el texto la letra g.
+ [ends-with(., "n")] : Realiza busqueda con coincidencias de textos que finalizan con la letra n.
+ [matches(., "*regex*")] : Realiza busqueda que coincidan en el texto con la expresion regular declarada.

### XPath Axes
Tenemos también los XPath Axes, que sirve para poder traer los nodos relacionados con el actual, esto es, nodos padres, hijos, ascendentes o descendientes.

+ self::*node* : Devuelve el nodo que estamos.
+ parent::*node* : Devuelve el nodo padre del actual.
+ ancestor::*node* : Devuelve los nodos padres y abuelos del actual.
+ ancestor-or-self::*node* : Devuelve el nodo actual y sus ancendentes.
+ child::*node* : Devuelve los nodos hijos.
+ descendant::*node* : Devuelve los nodos hijos y nietos del actual.
+ descendant-or-self : Devuelve los nodos hijos, nietos y el actual.

### Referencias recomendadas
+ Cheatsheets de XPath y más en [devhints.io](https://devhints.io/xpath)
+ Página para prácticar el scrapeo aquí [toscrape.com](http://toscrape.com)