import os
import re

import xlwings as xw

def compileFunc():
    workdir_path = r'C:\Users\tianming\Desktop\xlsdeal'
    first_data_row = 3
    app=xw.App(visible=False, add_book=False)
    filenames = [x for x in os.listdir(workdir_path) if re.match('^[^~$]+.xlsx$', x) is not None]
    for f in filenames:
        filepath = r'{}\{}'.format(workdir_path, f)
        wb = app.books.open(filepath)
        ws = wb.sheets[0]
        nrows = ws.used_range.last_cell.row
        for i in range(first_data_row, nrows):
            index_num = ws.range('A{}'.format(i)).value
            frdx3 = ws.range('T{}'.format(i)).value
            frdx3je_org = ws.range('U{}'.format(i)).value
            frdx3je = 0.0
            if frdx3je_org is not None and isinstance(frdx3je_org, str):
                frdx3je = float(frdx3je_org)
            spn = ws.range('AP{}'.format(i)).value
            if index_num is not None and frdx3 is None and frdx3je > 0:
                ws.range('T{}'.format(i)).value = spn
        wb.save()
        wb.close()
    app.quit()

if __name__ == '__main__':
    compileFunc();