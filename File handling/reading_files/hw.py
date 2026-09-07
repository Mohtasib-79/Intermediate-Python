# Missing Invoice Numbers
#
# invoice_sequence.txt
#
# INV1001
# INV1002
# INV1003
# INV1005
# INV1006
# INV1008
# INV1009
#
# Question: Invoice numbers should be sequential. Find the missing invoice numbers.
#
# Expected:
#
# INV1004
# INV1007

# with open('invoice_sequence.txt', 'r') as f:
#     lines = f.readlines()
#     print(lines)
#     invoice_num = []
#     unique_id=set()
    
  
    
#     for line in lines:
#         line = line.strip()
#         # print(int(line[3::]))
#         inv_id = int(line[3::])
#         if inv_id not in unique_id:
#             unique_id.add(inv_id)
#     full_inv = set()
#     i = min (unique_id)
#     while i<= max(unique_id):
#         full_inv.add(i)
#         i+=1
        
#     print(full_inv)
#     print(unique_id)
#     missing_inv = full_inv - unique_id
#     for i in missing_inv:
        # print("INV"+str(i))
 

        



# Employee Working Impossible Hours
#
# work_log.txt
#
# E101,8
# E102,9
# E103,7
# E104,19
# E105,8
# E106,27
#
# Question: Find suspicious records where employees reportedly worked more than 16 hours in one day.
#
# Expected:
#
# E104,19
# E106,27

with open('work_log.txt', 'r') as f:
    for line in f:
        line = line.strip()
        words = line.split(",")
        if int(words[-1]) >= 12:
            print(line)
            # print(line)
    

  

# work_log = {"E101":8,"E102":9,"E103":7,"E104":19,"E105":8,"E106":27}
# mydict = {}
# for key, value in work_log.items():
#     if value > 12:
#         mydict[key] = value
# print(mydict)
   


