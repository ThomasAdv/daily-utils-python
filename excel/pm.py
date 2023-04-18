import os
import re

import xlwings as xw

def compileFunc():
    first_data_row = 2
    app=xw.App(visible=False, add_book=False)
    filepath = r'C:\Users\tianming\Desktop\pm.xlsx'
    target_filepath = r'C:\Users\tianming\Desktop\pm.sql'
    if os.path.exists(target_filepath):
        os.remove(target_filepath)
    f = open(target_filepath, "a")
    wb = app.books.open(filepath)
    ws = wb.sheets[0]
    nrows = ws.used_range.last_cell.row
    for i in range(first_data_row, nrows+1):
        merchant_id = ws.range('A{}'.format(i)).value
        created_time = ws.range('B{}'.format(i)).value
        f.write('update dj_car_life_merchant set created_date  = \'{}\' where merchant_id = {};'.format(created_time, merchant_id))
        f.write("\n")
    wb.close()
    app.quit()
    f.close();

if __name__ == '__main__':
    compileFunc();