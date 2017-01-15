from pylatex import Document, Tabular, Figure, Section, Subsection, Command
from pylatex.utils import italic, NoEscape
import array_builder
import cv_yml

if __name__ == '__main__':
    # Basic document
    print("hey")
    geometry_options = {"tmargin": "2cm", "lmargin": "2cm"}

    doc = Document(geometry_options=geometry_options)

    path = "../../cv_yml/test"
    f = cv_yml.read_folder(path, "data")

    array_builder.latex_table(doc, f, ['MinRMS', 'InitCenter'])

    doc.generate_tex('generated tex')
    tex = doc.dumps()  # The document as string in LaTeX syntax
