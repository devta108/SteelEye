"""
This module is responsible for unzipping folders
"""
import logging
import zipfile
logging.basicConfig(filename='./test.log', level=logging.INFO)


def unzip(zipped_file, unzipped_file_path):
    try:
        logging.info("File unzipping started...")
        with zipfile.ZipFile(zipped_file, "r") as f:
            f.extractall(unzipped_file_path)
        logging.info("File unzipped successfully")
        return True
    except Exception as e:
        logging.info(f'Error during extraction {str(e)}')
        return False
