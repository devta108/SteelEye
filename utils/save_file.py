"""
This module is responsible for getting response from web and saving XML document to local machine
"""
import logging
from utils import get_url_response
logging.basicConfig(level=logging.INFO)


def get_document(url=None, file_name=None):
    """
    :param url: the document url needed to be scraped
    :param file_name: name of the file
    """
    if url is None:
        logging.info("Provide valid URL")
        return None
    if file_name is None:
        logging.info('Provide valid file name')
        return None
    if file_name.endswith('.xml'):
        logging.info('Extracting the URL')
        r = get_url_response(url)
    else:
        logging.info("Provide correct file extension...")
        return None
    """
    There might be 2 possibility in our case either we will get xml or html document [in our case it will be xml]
    """
    if not r.ok:
        logging.info('Nothing found out of URL')
        return None
    logging.info('getting the extension of file to be saved as')
    with open(f"./resources/{file_name}", 'wb') as f:
        logging.info('Writing the document file')
        f.write(r.content)
    return f
