"""
Скрипт для создания sample_data/sales.xlsx.
Запустите из корня проекта: python lesson5/create_sample_data.py
Или из lesson5: python create_sample_data.py
"""
from pathlib import Path
from openpyxl import Workbook

# Работает при запуске из корня или из lesson5
script_dir = Path(__file__).parent
output_path = script_dir / "sample_data" / "sales.xlsx"

wb = Workbook()
ws = wb.active
ws.title = "Sales"

# Заголовки
headers = ["product", "quantity", "price", "date"]
ws.append(headers)

# Данные
data = [
    ["Laptop", 5, 250000, "2025-02-01"],
    ["Mouse", 25, 5000, "2025-02-02"],
    ["Monitor", 3, 120000, "2025-02-03"],
    ["Keyboard", 15, 15000, "2025-02-04"],
    ["Laptop", 8, 250000, "2025-02-05"],
    ["Chair", 12, 35000, "2025-02-06"],
    ["Mouse", 30, 5000, "2025-02-07"],
    ["Desk", 2, 45000, "2025-02-08"],
]

for row in data:
    ws.append(row)

wb.save(output_path)
print(f"Created {output_path}")
