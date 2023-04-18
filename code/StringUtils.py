import sys

from system.win import Win32clipboardUtils


def generateDifSameTable():
    # print("请输入base_result_colum,按ctrl+d结束:")
    # inputlines = []
    # for line in sys.stdin:
    #     inputlines.extend(line.split())
    # s = ''.join(inputlines)
    s = '''
    id, rule_type, goods_type_group_rule_id, goods_type, goods_type_name
    '''
    dict = {"dclgtgr": "dclgtgr"}
    list1 = []
    for key,value in dict.items():
        list2 = []
        for str in s.split(","):
            list2.append(f" {key}.{str.lstrip()} as {value}_{str.lstrip()}")
        list1.append(",".join(list2))
    result = ",\n\n".join(list1)
    Win32clipboardUtils.setText(result)
    print(f"已复制到剪切板：\n{result}")


def generateDMapstructConvertField():
    str = '''
    merchant_id, merchant_name, short_name, user_type, merchant_type, account_name,
    contact_name, phone, address, province_id, province_name, city_id, city_name, area_id,
    area_name, lng, lat, shop_photo, channel_type, account_status,
    region,stay_contact_name,stay_phone,division_test_flag,open_date, entry_date, source_type
    '''
    list = []
    for field in str.split(","):
        field = field.strip().replace('\n','')
        list.append(f'@Mapping(source = "{field}", target = "gmopa.{field}")')
    print(",\n".join(list))

if __name__ == '__main__':
    generateDifSameTable()