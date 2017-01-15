import yaml
import numpy as np
from os.path import isfile, isdir
import glob
from collections import defaultdict

def _opencv_matrix(p_loader, p_node):
    mapping = p_loader.construct_mapping(p_node, deep=True)
    mat = np.array(mapping["data"])
    if not(mapping["rows"] == 1 or mapping["cols"] == 1):
        mat.resize(mapping["rows"], mapping["cols"])
    return mat

def read_file(p_path):
    if not(isfile(p_path) and p_path.lower().endswith('.yml')):
        raise FileNotFoundError
    yaml.add_constructor(u"tag:yaml.org,2002:opencv-matrix", _opencv_matrix)
    with open(path) as fin:
        for i in range(2):
            fin.readline()
        return yaml.load(fin.read())

def read_folder(p_folderPath, p_fileName):
    if not(isdir(p_folderPath)):
        raise NotADirectoryError
    path = p_folderPath + "/" + p_fileName
    files = glob.glob(p_folderPath + "/" + p_fileName + "*.yml")
    if not files:
        raise FileNotFoundError

    dict = defaultdict(list)
    for f in files:
        d = read_file(f)
        for k, v in d.items():
            dict[k].append(v)
    return dict

# def read_folder(folder_path, file_name):
#     if not(isdir(folder_path)):
#         raise NotADirectoryError
#     path = folder_path + "/" + file_name
#     files = glob.glob(folder_path + "/" + file_name + "*.yml")
#     if not files:
#         raise FileNotFoundError
#     array = []
#     for f in files:
#         array.append(read_file(f))
#     return array
