def day2():
    with open("../resources/day2.txt") as file:
        lines = file.readlines()

    horizontal_position = 0
    depth_position = 0

    for line in lines:
        instructions = str.split(line)

        direction = instructions[0]
        units = int(instructions[1])

        if direction == "forward":
            horizontal_position += units
        elif direction == "down":
            depth_position += units
        else:
            depth_position -= units

    print(horizontal_position * depth_position)


def day2_2():
    with open("../resources/day2.txt") as file:
        lines = file.readlines()

    horizontal_position = 0
    depth_position = 0
    aim = 0

    for line in lines:
        instructions = str.split(line)

        direction = instructions[0]
        units = int(instructions[1])

        if direction == "forward":
            horizontal_position += units
            depth_position = depth_position + (aim * units)
        elif direction == "down":
            aim += units
        else:
            aim -= units

    print(horizontal_position * depth_position)


if __name__ == "__main__":
    day2()