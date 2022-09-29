"""
This module is responsible for getting response from web and saving XML document to local machine
"""
import logging
from utils import get_url_response
logging.basicConfig(level=logging.INFO)


def get_document(url=None, file_name='basic.xml') -> None:
    """
    :param url: the document url needed to be scraped
    :param file_name: name of the file
    """
    logging.info('Extracting the URL')
    r = get_url_response(url)
    """
    There might be 2 possibility in our case either we will get xml or html document [in our case it will be xml]
    """
    logging.info('getting the extension of file to be saved as')
    with open(f"./resources/{file_name}", 'wb') as f:
        logging.info('Writing the document file')
        f.write(r.content)