# with open('fruits.txt', 'w') as f:
    # f.write('Apples\nMangoes\nYellow')
    # f.writelines(['Apples\n', 'Mangoes\n', 'Yellow\n'])

#
# with open('fruits.txt', 'a') as f:
#     f.write('Apples\n')
#     f.writelines(['Apples\n', 'Mangoes\n', 'Yellow\n'])
#


# with open('apples.txt', 'r') as f:
#     print(f.read())


# with open('apples.txt', 'w') as f:
#     f.writelines(['Apples\n', 'Mangoes\n', 'Yellow\n'])


# with open('apples.txt', 'a') as f:
#     f.writelines(['Apples\n', 'Mangoes\n', 'Yellow\n'])


# with open('fruits.txt', 'r') as f:
#     content = f.read()
#
# with open('output.txt', 'w') as g:
#     g.write(content)

with open('invoice_sequence.txt', 'r') as f:
    unique_ids = set()
    for line in f:
        number = int(line[3:])
        unique_ids.add(number)
    print(unique_ids)

    full_ids = set()
    i = min(unique_ids)
    while i <= max(unique_ids):
        full_ids.add(i)
        i += 1

    missing_ids = full_ids - unique_ids
    total_ids = unique_ids | missing_ids
    sorted_ids = sorted(total_ids)
    total_ids = list(map(lambda element: f"INV{element}\n", sorted_ids))

    with open('invoice_sequence.txt', 'w') as g:
        g.writelines(total_ids)



# with open('missing_invoices.txt', 'w') as f:
#     f.writelines(missing_ids)



