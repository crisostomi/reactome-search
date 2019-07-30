import os
import shutil
import glob
import xml.etree.ElementTree as ET


def moveOutput():
    os.mkdir("./output")
    for file in glob.glob(r'./BioSystem*'):
        shutil.move(file, './output')

def flushOutput():
    shutil.rmtree('./output/', ignore_errors=True)

def parseFile(file):
    tree = ET.parse(file)
    return tree.getroot()


