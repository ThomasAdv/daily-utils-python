import os
import re

import xlwings as xw

def compileFunc():
    first_data_row = 2
    app=xw.App(visible=False, add_book=False)
    filepath = r'C:\Users\tianming\Desktop\excel\by_order.xlsx'
    target_filepath = r'C:\Users\tianming\Desktop\excel\by_order.sql'
    if os.path.exists(target_filepath):
        os.remove(target_filepath)
    f = open(target_filepath, "a")
    wb = app.books.open(filepath)
    ws = wb.sheets[0]
    nrows = ws.used_range.last_cell.row
    f.write("insert into dj_car_life_audit_order_service_shop (order_code, install_merchant_name, marketing_merchant_name) values \n")
    for i in range(first_data_row, nrows+1):
        order_code = ws.range('A{}'.format(i)).value
        ins_m = ws.range('B{}'.format(i)).value
        mark_m = ws.range('C{}'.format(i)).value
        f.write('(\'{}\',\'{}\',\'{}\'),'.format(order_code, ins_m, mark_m))
        f.write("\n")
    wb.close()
    app.quit()
    f.close();

if __name__ == '__main__':
    compileFunc();