import xlrd

import xlwings as xw

def compileFunc():
    filepath = r'C:\Users\tianming\Desktop\by_order.xlsx'
    data = xlrd.open_workbook(filepath)
    table = data.sheets()[0]
    nrows = table.nrows

    for i in range(1, nrows):
        order_code = table.cell(i, 0).value
        ins_m = table.cell(i, 1).value
        mkt_m = table.cell(i, 2).value
        string = 'OrderCode:' + str(order_code) + 'Ins_m' + str(ins_m) + 'Mkt_m' + str(mkt_m)
        print(string)

if __name__ == '__main__':
    compileFunc();