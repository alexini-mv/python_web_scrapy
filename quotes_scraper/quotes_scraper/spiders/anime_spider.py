from turtle import title
import scrapy


class AnimeSpider(scrapy.Spider):
    # Nombre del spider. Debe ser único ya que con él se identificará el script
    name = "jkanime"

    # URLs a las que apuntaremos
    start_urls = [
        "https://jkanime.net/amagami-ss/1/"
    ]

    # Propiedades para guardar los resultados
    custom_settings = {
        "FEEDS": {
            "resultados.csv": {
                "format": "csv",
                "encoding": "utf8",
                "store_empty": False,
                "fields": None,
                "indent": 4,
                "overwrite": True
            }
        }
    }

    def parse(self, response):
        # Las instrucciones para parsear los datos de interés
        title = response.xpath(
            '//div[@class="breadcrumb__links"]/h1/text()').get()

        # Los campos que queremos guardar
        yield {
            "Titulo del episodio": title
        }

        # Sección para hacer seguimiento entre páginas.
        next_page = response.xpath(
            '//i[@class="arrow_right-down"]/ancestor::a/@href').get()
        if next_page:
            yield response.follow(
                next_page,
                callback=self.parse
                
                # callback=self.parse_only_title,
                #cb_kwargs={"title": [title]}
            )

    # Definición alternativa para guardarlo como una sola lista
    # def parse_only_title(self, response, **kwargs):
    #     if kwargs:
    #         title = kwargs["title"]

    #     aux_title = response.xpath(
    #         '//div[@class="breadcrumb__links"]/h1/text()').get()
    #     title.append(aux_title)

    #     next_page = response.xpath(
    #         '//i[@class="arrow_right-down"]/ancestor::a/@href').get()

    #     if next_page:
    #         yield response.follow(
    #             next_page,
    #             callback=self.parse_only_title,
    #             cb_kwargs={"title": title}
    #         )
    #     else:
    #         yield {
    #             "Titulo del episodio": title
    #         }
