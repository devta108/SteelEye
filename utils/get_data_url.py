"""
This module will help us to get the dataurl from which we will convert it to csv format
"""
import logging
import xml.etree.ElementTree as ET
logging.basicConfig(filename='./test.log', level=logging.INFO)


def get_data_url(basic_filepath=None):
    """
    This will return link for the data and it's name
    :param basic_filepath: This is basic xml document path that we saved from base_url
    """
    if basic_filepath is None:
        logging.info("Provide basic file path")
        exit(1)
    et_obj = ET.parse(basic_filepath)
    root = et_obj.getroot()[1]
    docs = root.findall('doc')
    for doc in docs:
        logging.info("Extracting the file type")
        file_type = doc.find(".//str[@name='file_type']")

        if file_type.text == "DLTINS":
            '''
            getting first download link as per the problem
            '''
            logging.info("Match found for file type DLTINS")
            logging.info("Extracting file name")
            file_name = doc.find(".//str[@name='file_name']").text
            logging.info("Extracting the file download link")
            download_link = doc.find(".//str[@name='download_link']").text
            break
        else:
            logging.info("Match not found for file type DLTINS")
            return None

    return file_name, download_link

