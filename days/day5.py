import copy

def day5():
    with open("../resources/day5.txt") as f:
        lines = f.readlines()

    listofzeros = [0] * 1000

    playing_field = []
    for i in range (0, 1000):
        playing_field.append(copy.deepcopy(listofzeros))

    for input_line in lines:
        coordinates = input_line.rstrip().split("->")

        first_coor = coordinates[0].split(",")
        second_coor = coordinates[1].split(",")

        x1 = int(first_coor[0])
        y1 = int(first_coor[1])

        x2 = int(second_coor[0])
        y2 = int(second_coor[1])

        if x1 == x2:
            if y1 < y2:
                for i in range(y1, y2+1):
                    playing_field[x1][i] += 1
            else:
                for i in range(y2, y1+1):
                    playing_field[x1][i] += 1
        elif y1 == y2:
            if x1 < x2:
                for i in range(x1, x2+1):
                    line = playing_field[i]
                    line[y1] += 1
            else:
                for i in range(x2, x1 + 1):
                    line = playing_field[i]
                    line[y1] += 1
        else:
            if x1 < x2:
                if y1 < y2:
                    y = y1
                    for i in range(x1, x2+1):
                            playing_field[i][y] += 1
                            y+=1
                else:
                    y = y1
                    for i in range(x1, x2 + 1):
                        playing_field[i][y] += 1
                        y -= 1
            else:
                if y1 < y2:
                    y = y1
                    x=x1
                    while x >= x2:
                        playing_field[x][y] += 1
                        y += 1
                        x-=1
                else:
                    y = y1
                    x=x1
                    while x >= x2:
                        playing_field[x][y] += 1
                        y-=1
                        x-=1

    crossing_lines = 0
    for line in playing_field:
        for count in line:
            if count > 1:
                crossing_lines+=1

    print(crossing_lines)





if __name__ == "__main__":
    day5()