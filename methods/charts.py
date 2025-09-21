from time import sleep

# Get data

def get_list_tables(workbook):
    """ Возвращает список таблиц в документе """
    sheets = map(lambda x: x.title, workbook.worksheets())
    print(list(sheets))
    return list(sheets)


def get_cols_name(workbook):
    """ Возвращает названия колонок """
    values_list = workbook.sheet1.row_values(1)
    print(values_list)
    return values_list


def get_cols_rows(workbook, rows):
    """ Возвращает названия колонок """
    values_list = {}
    for row in rows:
        data = workbook.sheet1.row_values(row)
        values_list[row] = data
        print(f"\nROW { row } : lenght = { len(data) } : { data }\n\t-----")
    return values_list


def get_cols(workbook):
    """ Возвращает названия колонок """
    values_list = workbook.sheet1.get_all_values()
    print(values_list)
    return values_list



# Update data
def test_update_data(workbook):
    data4 = ['з/ч', 'Кабель ток', 'СК.00.01', 'Клемма круглая', 'Готово, 2', '5,00', '20.09.2025', '', '', '', '', '2, 3', '16.09.2025', '17.09.2025', '120,00', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '1', '16.09.2025', '', '120,00', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '3', '', '', '', '18.09.2025']
    workbook.sheet1.update('A4:CO4', [data4])
    
    sleep(5)
    data4 = ['з/ч', 'Кабель ток', 'СК.00.01', 'Клемма круглая', 'Готово, 2', '5,00', '20.09.2025', '', '', '', '', '2, 3', '16.09.2025', '17.09.2025', '120,00', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '1', '16.09.2025', '', '120,00', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '3', '', '', '', '']
    workbook.sheet1.update('A4:CO4', [data4])
