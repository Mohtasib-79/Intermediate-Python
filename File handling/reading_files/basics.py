# opening
# close

# with open('fruits.txt', 'r') as f:
#     content = f.read()
#     print(content)
    # print(type(content))
    # print(content[0])
    # content = content.split()
    # print(content[0])

# with open('fruits.txt', 'r') as f:
#     content = f.readlines()
#     print(content)


# with open('fruits.txt', 'r') as f:
#     content = f.readline()
#     print(content)
#     c = f.readlines()
#     print(c)

# with open('fruits.txt', 'r') as f:
#     # for i in range(5):
#     #     next(f)
#     next(f) # moving the pointer to next line
#     c = f.readlines()
#     print(c)


# with open('fruits.txt', 'r') as f:
    # print(f) # lazy iterator
    # print(list(range(1, 5))) # lazy

    # for line in f:
    #     print(line, type(line))


# with open('fruits.txt', 'r') as f:
#     for line in f:
#         print(line)


# # Q1. Count how many characters
# with open('fruits.txt', 'r') as f:
#     content = f.read()
#     print(len(content))
#
#     # count = 0
#     # for i in range(len(content)):
#     #     count += 1
#     # print(count)



# # Q1. Count how many lines
# with open('fruits.txt', 'r') as f:
#     content = f.readlines()
#     print(len(content))



# Q1. Count how many words
# with open('fruits.txt', 'r') as f:
#     count = 0
#     for line in f:
#         line = line.split()
#         count += len(line)
#     print(count)

# Q. Search if apple exists
# with open('fruits.txt', 'r') as f:
#     content = f.read()
#     if 'APPLE' in content.upper():
#         print("Found")
#     else:
#         print("Not Found")


# Q. Search if apple exists and in which line?
# with open("fruits.txt", 'r') as f:
#     line_num = 0
#     for line in f:
#         line_num += 1
#         if 'apple' in line.lower():
#             print(f"Found at line number {line_num}")


# word = input("Enter the word: ")
# with open('fruits.txt', 'r') as f:
#     for line in f:
#         if word in line:
#             words = line.split()
#             for i in range(len(words)):
#                 if word == words[i]:
#                     print(words[i], words[i+2])

