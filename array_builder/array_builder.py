from pylatex import Tabular
import numpy as np

def latex_table(p_doc, p_dict, p_order = [], p_columnsName = {}, p_firstColumn = []):
    order = []
    if len(p_order) == 0:
        order = list(p_dict.keys())
    else:
        order = p_order

    cols = []
    if len(p_columnsName) == 0:
        cols = {key : key for key in order}
    else:
        cols = p_columnsName

    columnsName = []
    for o in order:
        columnsName.append(cols[o])

    tabCols = '|'
    for i in range(len(order)):
        tabCols += 'c|'

    with p_doc.create(Tabular(tabCols)) as table:
        table.add_hline()
        table.add_row(columnsName)
        table.add_hline()

        for n in range(len(p_dict[order[0]])):
            table.add_hline()
            row = []
            for k in order:
                row.append(p_dict[k][n])
            table.add_row(row)
    table.add_hline()
