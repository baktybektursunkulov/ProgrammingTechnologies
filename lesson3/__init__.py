grades = {}
with open('test.txt') as f:
    for line in f:
        name, grade = line.strip().split(',')
        grades[name] = int(grade)
    print(grades)
with open('test.txt', 'a') as fileWrite:
    fileWrite.write("Test3,90\n")
    fileWrite.write("Test2,85\n")
# import csv
#
# students = []
# with open('testcsv.csv') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         students.append(row)
# print(students)

# wb = load_workbook('students.xlsx')
# sheet = wb.active
# students = {}
# for row in sheet.iter_rows(min_row=2, values_only=True):
#     name, age = row
#     students[name] = age

# import json
# with open('data.json') as f:
#     data = json.load(f)
# print(data)
# with open('summary.json','w', encoding='utf-8') as f:
#     json.dump(data, f, indent=4)




