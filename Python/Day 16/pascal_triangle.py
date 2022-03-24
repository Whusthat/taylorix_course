def tri(n):
    # list to keep track of all rows in case we need them for later use
    all_rows = [[1]]
    # we start with row 1
    current_row = [1]
    # n represents the level (height) of the triangle
    # so each n represents one row
    for i in range(1, n):
        # for the new row we take the first index of current_row which is always == 1
        new_row = [1]
        # go over every number in row -1 (so we don't run an index error if we would call j + 1 on the last element
        for j in range(len(current_row) - 1):
            # append added elements from current_row -> new_row
            new_row.append(current_row[j] + current_row[j + 1])
            # append the 1 again to end the new row
        new_row += [1]
        # add new row to all_row list
        all_rows += [new_row]
        # set new row to current_row
        current_row = new_row

    return current_row, all_rows, n


def main():
    nth_row, all_rows, n = tri(7)
    print(f"The {n}. Row of the Triangle is {nth_row}")
    result = all_rows
    max_length = len(result)
    for i in range(1):
        print((max_length-i) * '', result)


if __name__ == '__main__':
    main()