raw_grid = open("11.txt", "r")

grid = raw_grid.readlines()
raw_grid.close()
print(grid)

for row_n in range(0, len(grid)):
    grid[row_n] = grid[row_n].replace("\n", "")
    grid[row_n] = grid[row_n].split(" ")
print(grid)

size_x = len(grid[0])
size_y = len(grid)
print("size: %i x %i" % (size_x, size_y))
products = []

for row_pos in range(size_y):

    for base_pos in range(0, size_x - 4 + 1):
        selection = []
        selection_product = 1
        for str_number_pos in range(base_pos, base_pos + 4):
            selection.append(grid[row_pos][str_number_pos])
        for str_number in selection:
            selection_product *= int(str_number)
        products.append(selection_product)
        print("horizontal %s position %s prod %s" % (selection, len(products) - 1, selection_product))

for col_pos in range(size_x):
    for base_pos in range(0, size_y - 4 + 1):
        selection = []
        selection_product = 1
        for str_number_pos in range(base_pos, base_pos + 4):

            selection.append(grid[str_number_pos][col_pos])
        for str_number in selection:
            selection_product *= int(str_number)
        products.append(selection_product)
        print("vertical %s position %s prod %s" % (selection, len(products) - 1, selection_product))

selections = []
part_selection = []

fr = 0
for col in range(0, size_y - 4 + 1):
    for row in range(0, size_x - 4 + 1):
        fr += 1

for each in range(fr):
    selections.append([])

for step in range(1, 5):
    for col in range(step - 1, size_x - 4 + step):
        for row in range(step - 1, size_y - 4 + step):
            part_selection.append(grid[col][row])
    for element_pos in range(fr):
        selections[element_pos].append(part_selection[element_pos])
    part_selection = []

for list_inside in selections:
    selection_product = 1
    for str_number in list_inside:
        selection_product *= int(str_number)
    products.append(selection_product)
    print("diagonal R %s position %s prod %s" % (list_inside, len(products) - 1, selection_product))

selections = []
part_selection = []

for each in range(fr):
    selections.append([])

for step in range(1, 5):
    for col in range(3 - step + 1, size_x + 1 - step):
        for row in range(step - 1, size_y - 4 + step):
            part_selection.append(grid[col][row])
    for element_pos in range(fr):
        selections[element_pos].append(part_selection[element_pos])
    part_selection = []

for list_inside in selections:
    selection_product = 1
    for str_number in list_inside:
        selection_product *= int(str_number)
    products.append(selection_product)
    print("diagonal L %s position %s prod %s" % (list_inside, len(products) - 1, selection_product))

print("- - - - - - - - - - -")
print("max product: %i" % max(products))
print("position of max: %i" % products.index(max(products)))
print("- - - - - - - - - - -")
