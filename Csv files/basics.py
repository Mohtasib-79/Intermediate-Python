import csv
# modules -> folder

# with open('products.csv', 'r') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row[3])


# with open('products.csv', 'r') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row['quantity'])


# Print products costing more than ₹10,000.
# with open('products.csv', 'r') as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         if int(row['price']) > 10_000:
#             print(row['product'])


# Calculate total number of products in stock.
# Answer:
#
# 46
# with open('products.csv', 'r') as f:
#     # for i in range(3):
#     #     next(f)
#     next(f)
#     reader = csv.reader(f)
#     quantity = 0
#     for row in reader:
#         quantity += int(row[3])
#     print(quantity)

# with open('data.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(['name', 'city', 'product'])
#
#     writer.writerow(['Raj', 'Delhi', 'Cooler'])
#     writer.writerow(['Rahul', 'Delhi', 'AC'])

# rows = [['Raj', 'Delhi', 'AC'], ['Raj', 'Delhi', 'Cooler']]
# with open('data.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(['name', 'city', 'product'])
#
#     writer.writerows(rows)

# fieldnames = ['name', 'city', 'product']
# with open('data.csv', 'w') as f:
#     writer = csv.DictWriter(f, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({'name': 'Raj', 'city': 'Mumbai', 'product': 'AC'})


# Find total revenue from all sales.
# with open('sales.csv', 'r') as f:
#     total_sales = 0
#     reader = csv.DictReader(f)
#     for row in reader:
#         total_sales += (int(row['quantity']) * float(row['price']))
#
#     print(total_sales)
#
# with open('sales_report.txt', 'w') as g:
#     g.write(str(total_sales))


# find total sales per product
# with open('sales.csv', 'r') as f:
#     sales_dict = {}
#     reader = csv.DictReader(f)
#     for row in reader:
#         product = row['product']
#         revenue = int(row['quantity']) * float(row['price'])
#         if product not in sales_dict:
#             sales_dict[product] = revenue
#         else:
#             sales_dict[product] += revenue
#
#     print(sales_dict)

