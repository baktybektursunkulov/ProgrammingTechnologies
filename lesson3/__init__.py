# grades = {}
# with open('C:\\Users\\1\\Desktop\\test.txt') as f:
#     print(f.read())
#     # file = open('C:\\Users\\1\\Desktop\\test.txt')
#     # file.
#     # f.close()
#     for line in f:
#         name, grade = line.strip().split(',')
#         grades[name] = int(grade)
#     print(grades)
# file = open('C:\\Users\\1\\Desktop\\test.txt')
# file.writable()
# file.write(file.)
# file.close()

# import csv
#
# students = []
# with open('') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         students.append(row)
# print(students)

# wb = load_workbook('students.xlsx')
# sheet = wb.activeC:\\Users\\1\\Desktop\\testcsv.csv
# students = {}
# for row in sheet.iter_rows(min_row=2, values_only=True):
#     name, age = row
#     students[name] = age

import json
with open('C:\\Users\\1\\Desktop\\data.json') as f:
    data = json.load(f)
print(data)
with open('summary.json','w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)




