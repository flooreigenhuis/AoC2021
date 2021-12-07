def day1():
    with open("../resources/day1.txt") as file:
        lines = file.readlines()

    previous_depth = None
    count = 0

    for line in lines:
        depth = int(line.rstrip())
        if previous_depth:
            if previous_depth < depth:
                count += 1
        previous_depth = depth

    print(count)


def day1_2():
    with open("../resources/day1.txt") as file:
        lines = file.readlines()

    previous_depth = 0
    count = 0
    one_depth_ago = 0
    two_depths_ago = 0

    for line in lines:
        depth = int(line.rstrip())
        current_depth = depth + one_depth_ago + two_depths_ago
        if previous_depth:
            if previous_depth < current_depth:
                count += 1

        if one_depth_ago and two_depths_ago:
            previous_depth = current_depth
        two_depths_ago = one_depth_ago
        one_depth_ago = depth

    print(count)


if __name__ == "__main__":
    day1()
