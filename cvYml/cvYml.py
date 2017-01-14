import yaml
import numpy as np
from os.path import isfile

class cvYml:

    @staticmethod
    def _opencv_matrix(loader, node):
        mapping = loader.construct_mapping(node, deep=True)
        mat = np.array(mapping["data"])
        mat.resize(mapping["rows"], mapping["cols"])
        return mat

    def __init__(self, path):
        if not(isfile(path) and path.lower().endswith('.yml')):
            raise FileNotFoundError
        self.path = path

    def read(self):
        yaml.add_constructor(u"tag:yaml.org,2002:opencv-matrix", cvYml._opencv_matrix)
        with open(self.path) as fin:
            for i in range(2):
                fin.readline()
            return yaml.load(fin.read())
