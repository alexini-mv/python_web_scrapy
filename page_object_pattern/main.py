from random import choices
from common import config
import argparse
from asyncio.log import logger
import logging
logging.basicConfig(level=logging.INFO)


logger = logging.getLogger(__name__)


def _new_scraper(new_site_name):
    host = list(config()['new_sites'][new_site_name].keys())

    logging.info(f"Beginning scraper for {host}")


if __name__ == "__main__"
    parser = argparse._ArgumentParser()

    new_site_choices = list(config()['new_sites'].keys())
    parser.add_argument("news_site",
                        help="The news site that you can to scrape",
                        type=str,
                        choices=new_site_choices)

    args = parser.parse_args()

    _new_scraper(args.new_site)