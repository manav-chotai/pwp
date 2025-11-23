import pandas as pd
excel_file_path = 'sample_data.xlsx'
df_excel = pd.read_excel(excel_file_path)
# Save DataFrame to a new Excel file
df_excel.to_excel('new_data.xlsx', index=False)
print("Excel data saved to 'new_data.xlsx'.")
