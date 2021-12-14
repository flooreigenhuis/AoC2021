import copy

routes = []


def day12():
    with open("../resources/day12_test.txt") as f:
        lines = f.readlines()

    cave_map = {}
    for line in lines:
        connection = line.replace("\n", "").split("-")

        if connection[0] not in cave_map.keys():
            cave_map[connection[0]] = [connection[1]]
        else:
            cave_map[connection[0]].append(connection[1])

        if connection[1] not in cave_map.keys():
            cave_map[connection[1]] = [connection[0]]
        else:
            cave_map[connection[1]].append(connection[0])


    starting_points = cave_map["start"]

    for starting_point in starting_points:
        points_visited = ["start"]
        find_connected_points(points_visited, starting_point, cave_map)

    print(routes)
    print(len(routes))


def find_connected_points(points_visited, starting_point, cave_map):

    for following_point in cave_map[starting_point]:
        if following_point == "end":
            if points_visited + [starting_point, "end"] not in routes:
                routes.append(points_visited + [starting_point, "end"])
            continue
        if following_point.isupper() or following_point not in points_visited:
            points_visited.append(starting_point)
            find_connected_points(points_visited, following_point, cave_map)


if __name__ == "__main__":
    day12()
