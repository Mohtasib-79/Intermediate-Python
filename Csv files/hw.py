# Read employees.csv using csv.reader() and print every employee record except the header.

# Print all employees earning more than 50000.

# Count how many employees belong to each department.
#
# Expected type of result:
#
# {
#     "Sales": 2,
#     "IT": 3,
#     "HR": 1,
#     "Finance": 2
# }

# Find the employee with the highest salary. Print their name, department, and salary.

# Calculate the average salary separately for each department.

# Find which city has the highest number of employees.

# Read employees.csv using csv.reader() and print every employee record except the header.
import csv
# with open('employees.csv', 'r') as f:
#     reader = csv.reader(f)
#     next(reader)
#     for row in reader:
#         print(row)

# # Print all employees earning more than 50000.
# with open('employees.csv','r') as f:
#     reader = csv.reader(f)
#     next(reader)
#     for row in reader:
#             if int(row[3]) > 50000:
#                 print(row[1])
# # Count how many employees belong to each department.
# with open('employees.csv','r') as f:
# dept_count = {}
# for row in employees:
#     dept = row[2]
#     if dept in dept_count:
#         dept_count[dept] += 1
#     else:
#         dept_count[dept] = 1
# print(dept_count)

# with open('employees.csv','r') as f:
# top = employees[0]
# for row in employees:
#     if int(row[3]) > int(top[3]):
#         top = row
# print("ID:", top[0])
# print("Name:", top[1])
# print("Department:", top[2])
# print("Salary:", top[3])

# # Average salary per department 
# dept_total  = {}
# dept_count2 = {}
# for row in employees:
#     dept   = row[2]
#     salary = int(row[3])
#     if dept in dept_total:
#         dept_total[dept]  += salary
#         dept_count2[dept] += 1
#     else:
#         dept_total[dept]  = salary
#         dept_count2[dept] = 1
# for dept in dept_total:
#     avg = dept_total[dept] / dept_count2[dept]
#     print(dept, ":", avg)

# # City with most employees 
# city_count = {}
# for row in employees:
#     city = row[4]
#     if city in city_count:
#         city_count[city] += 1
#     else:
#         city_count[city] = 1
# print(city_count)

# top_city  = ""
# top_count = 0
# for city, count in city_count.items():
#     if count > top_count:
#         top_count = count
#         top_city  = city
# print("City with most employees:", top_city, "-", top_count)