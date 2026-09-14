# Write only reviews containing the word "bad" into negative_reviews.txt.
#
# Example input:
#
# The product is good
# Delivery was bad
# Very useful product
# Bad packaging
#
# Expected output:
#
# Delivery was bad
# Bad packaging
# ........................................................
# with open("negative_reviews.txt", "r") as f:
#     lines = f.readlines()

# with open("review_analysis.txt", "w") as g:
#     for line in lines:
#         if "bad" in line.lower():
#             g.write(line)
# ..........................................................

 
# server_log.txt:
#
# INFO Server started
# ERROR Database connection failed
# INFO User logged in
# ERROR API timeout
# WARNING Memory high
#
# Write only lines beginning with ERROR into errors.txt.

# ...................................................................
# with open("server_log.txt","r") as f:
#     lines = f.readlines()
#     # print(lines)

# with open("error_log.txt", "w") as g:
#     for line in lines:
#         if line.strip().startswith("ERROR"):
#             g.write(line)

# ......................................................................



# marks.txt:
#
# Aman,78
# Riya,32
# Karan,65
# Neha,29
# Sam,90
#
# Read the file and write students having marks below 40 into failed_students.txt.
#
# Expected:
#
# Riya,32
# Neha,29
with open("marks.txt","r") as f:
    lines = f.readlines()
    # print(lines)
with open("failed_students.txt", "w") as g:
    for line in lines:
        student_marks = line.strip().split(",")
        mark = float(student_marks[1])
        # print(mark)
        if mark < 40:
            g.write(line)



