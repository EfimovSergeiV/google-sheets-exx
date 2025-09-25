import gspread
from google.oauth2.service_account import Credentials

from methods.parsers import *
from methods.sheets import *
from conf import sheet_id


scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

workbook = client.open_by_key(sheet_id)




# get_list_tables(workbook)
# print("\n-----\n")
# get_cols_name(workbook)
# get_list_rows(workbook, [1,3])



# Скачиваем все данные, для работы локально
# all_data = get_all_rows(workbook)
# with open("all_data.txt", "w", encoding="utf-8") as f:
#     f.write(all_data.__str__())

import_data_from_file()




# test_update_data(workbook)
# test_insert_data(workbook)




# workbook = client.open_by_key(sheet_id)

# values = [
#     ["Name", "Price", "Quantity"],
#     ["Basketball", 29.99, 1],
#     ["Jeans", 39.99, 4],
#     ["Soap", 7.99, 3],
# ]

# worksheet_list = map(lambda x: x.title, workbook.worksheets())
# new_worksheet_name = "Values"

# if new_worksheet_name in worksheet_list:
#     sheet = workbook.worksheet(new_worksheet_name)
# else:
#     sheet = workbook.add_worksheet(new_worksheet_name, rows=10, cols=10)

# sheet.clear()

# sheet.update(f"A1:C{len(values)}", values)

# sheet.update_cell(len(values) + 1, 2, "=sum(B2:B4)")
# sheet.update_cell(len(values) + 1, 3, "=sum(C2:C4)")

# sheet.format("A1:C1", {"textFormat": {"bold": True}})
