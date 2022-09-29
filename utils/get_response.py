"""
    This module is responsible for responses for the provided url
"""
import logging
import os
import requests
logging.basicConfig(filename='test.log', level=logging.INFO)


def get_url_response(url=None):
    """
    This method is responsible for getting http/https response from web and returning the same data
    :param url:
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/93.0.4577.63 Safari/537.36 ',
        'Connection': 'keep-alive',
        'Accept': '*/*'
    }
    r = requests.get(url, headers=headers)
    logging.info(f'GET api response {r.status_code}')
    return r
