import yaml
import numpy as np
from os.path import isfile, isdir
import glob

def _opencv_matrix(loader, node):
    mapping = loader.construct_mapping(node, deep=True)
    if mapping["rows"] == 1 or mapping["cols"] == 1:
        return mapping["data"]
    mat = np.array(mapping["data"])
    mat.resize(mapping["rows"], mapping["cols"])
    return mat

def read_file(path):
    if not(isfile(path) and path.lower().endswith('.yml')):
        raise FileNotFoundError
    yaml.add_constructor(u"tag:yaml.org,2002:opencv-matrix", _opencv_matrix)
    with open(path) as fin:
        for i in range(2):
            fin.readline()
        return yaml.load(fin.read())

def read_folder(folder_path, file_name):
    if not(isdir(folder_path)):
        raise NotADirectoryError
    path = folder_path + "/" + file_name
    files = glob.glob(folder_path + "/" + file_name + "*.yml")
    if not files:
        raise FileNotFoundError
    array = []
    for f in files:
        array.append(read_file(f))
    return array
