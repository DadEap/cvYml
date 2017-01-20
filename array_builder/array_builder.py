from pylatex import Tabular, LineBreak
import numpy as np

def latex_table(p_doc, p_dict, p_order = [], p_columnsName = {}, p_firstColumnName = ""):

    order = []
    if len(p_order) == 0:
        order = list(p_dict.keys())
    else:
        order = p_order

    lengthDictArrays = len(p_dict[order[0]])

    cols = {}
    if len(p_columnsName) == 0:
        cols = {key : key for key in order}
    else:
        for i in p_order:
            if i in p_columnsName.keys():
                cols[i] = p_columnsName[i]
            else :
                cols[i] = i

    columnsName = [""]
    for o in order:
        columnsName.append(cols[o])

    fcol = []
    if p_firstColumnName:
        if p_firstColumnName in p_dict.keys():
            fcol = p_dict[p_firstColumnName]
        else:
            for i in range(lengthDictArrays):
                fcol.append(p_firstColumnName + " " + str(i+1))
    else:
        for i in range(lengthDictArrays):
            fcol.append(i+1)

    tabCols = '|'
    for i in range(len(order) + 1):
        tabCols += 'c|'

    with p_doc.create(Tabular(tabCols)) as table:

        table.add_hline()
        table.add_row(columnsName)
        table.add_hline()

        for i, n in enumerate(range(lengthDictArrays)):
            table.add_hline()
            row = [fcol[i]]
            for k in order:
                row.append(p_dict[k][n])
            table.add_row(row)
    table.add_hline()

    p_doc.append(LineBreak())
