import statistics

def day7():
    with open("../resources/day7.txt") as f:
        lines = f.read()

    horizontal_positions = list(map(int, lines.split(",")))

    median = statistics.median(horizontal_positions)

    fuel = 0
    for horizontal_position in horizontal_positions:
        fuel += abs(horizontal_position - median)

    print(fuel)

def day7_2():
    with open("../resources/day7.txt") as f:
        lines = f.read()

    horizontal_positions = list(map(int, lines.split(",")))

    position = int(statistics.mean(horizontal_positions))

    fuel = 0
    for horizontal_position in horizontal_positions:
        fuel += sum((list(range(abs(horizontal_position - position)+1))))

    print(fuel)


if __name__ == "__main__":
    day7_2()