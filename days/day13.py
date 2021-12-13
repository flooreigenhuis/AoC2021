import copy


def day13():
    folds = [["x", 655], ["y", 447], ["x", 327], ["y", 223], ["x", 163],
             ["y", 111], ["x", 81], ["y", 55], ["x", 40], ["y", 27], ["y", 13],
             ["y", 6]]

    # folds = [["y", 7], ["x", 5]]

    with open("../resources/day13.txt") as f:
        lines = f.readlines()

    field = [[0] * 1311 for i in range(0,895)]

    # field = [[0] * 11 for i in range(0, 15)]

    for line in lines:
        coordinates = line.split(",")

        x = int(coordinates[0])
        y = int(coordinates[1])

        field[y][x] = 1


    for fold in folds:
        new_field = []

        fold_line = fold[1]
        # vertical fold
        if fold[0] == "x":
            for line in field:
                max_index = len(line) -1

                new_line = []
                for i in range(0, fold_line):
                    new_line.append(max(line[i], line[max_index - i ]))

                new_field.append(new_line)
        else:
            for line_idx in range(0, fold_line):
                new_line = []
                line = field[line_idx]
                max_line = len(field) - 1
                for number_idx in range(0, len(line)):
                    new_line.append(max(line[number_idx], field[max_line - line_idx][number_idx]))
                new_field.append(new_line)

        field = copy.deepcopy(new_field)

    counter = 0
    for line in field:
        print_line = []
        for char in line:
            if char == 0:
                print_line.append(".")
            else:
                print_line.append("#")
        print(print_line)


    print(counter)

        


if __name__ == "__main__":
    day13()