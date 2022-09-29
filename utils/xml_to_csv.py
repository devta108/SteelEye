"""
XML data to csv parsing
"""
import xml.etree.ElementTree as ET
import csv
import os


def extract_data_to_csv(xml_path, csv_path):
    """

    :param xml_path: xml data path
    :param csv_path: final destination path
    """
    tree = ET.parse(xml_path)
    root = tree.getroot()
    headers = set(['Id', 'FullNm', 'ClssfctnTp', 'CmmdtyDerivInd', 'NtnlCcy', 'Issr'])
    data = {
        'Id': "",
        'FullNm': "",
        'ClssfctnTp': "",
        'CmmdtyDerivInd': "",
        'NtnlCcy': "",
        'Issr': ""
    }
    for elem in root.iter():
        tag = elem.tag
        if 'TermntdRcrd' in tag:
            for child in elem.iter():
                child_tag = child.tag.split('}')[-1]
                if child_tag == 'FinInstrmGnlAttrbts':
                    for gchild in child.iter():
                        gtag = gchild.tag.split('}')[-1]
                        if gtag in data:
                            data[gtag] = gchild.text
                if child_tag == 'Issr':
                    data[child_tag] = child.text
            writer = csv.writer(open(csv_path, 'a', newline=''))
            writer.writerow(
                [data['Id'],
                 data['FullNm'],
                 data['ClssfctnTp'],
                 data['CmmdtyDerivInd'],
                 data['NtnlCcy'],
                 data['Issr']
                 ])
