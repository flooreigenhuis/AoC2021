def day9():
    with open("../resources/day9.txt") as f:
        lines = f.readlines()

    height_maps = [list(map(int, line.replace("\n", ""))) for line in lines]
    risk_level = 0

    for map_idx, height_map in enumerate(height_maps):
        for height_idx, height in enumerate(height_map):
            # horizontal neighbors
            if height_idx + 1 < len(height_map):
                if height >= height_map[height_idx + 1]:
                    continue

            if height_idx > 0:
                if height >= height_map[height_idx - 1]:
                    continue

            # vertical neighbors
            if map_idx + 1 < len(height_maps):
                if height >= height_maps[map_idx+1][height_idx]:
                    continue

            if map_idx > 0:
                if height >= height_maps[map_idx-1][height_idx]:
                    continue

            risk_level += height + 1



    print(f"risk level: {risk_level}")

def day9_2():
    with open("../resources/day9.txt") as f:
        lines = f.readlines()

    height_maps = [list(map(int, line.replace("\n", ""))) for line in lines]

    basins = [1, 2, 3]

    for map_idx, height_map in enumerate(height_maps):
        for height_idx, height in enumerate(height_map):

            if height == 9:
                continue

            # horizontal neighbors
            if height_idx + 1 < len(height_map):
                if height >= height_map[height_idx + 1]:
                    continue

            if height_idx > 0:
                if height >= height_map[height_idx - 1]:
                    continue

            # vertical neighbors
            if map_idx + 1 < len(height_maps):
                if height >= height_maps[map_idx+1][height_idx]:
                    continue

            if map_idx > 0:
                if height >= height_maps[map_idx-1][height_idx]:
                    continue

            # make list of points_to_explore
            points_to_explore = [[map_idx, height_idx]]
            explored = [False]
            size = 0

            while not all(i for i in explored):
                size += 1

                for idx, value in enumerate(explored):
                    if not value:
                        point = idx
                        break

                i_map = points_to_explore[point][0]
                i_number = points_to_explore[point][1]

                # horizontal neighbors
                if i_number + 1 < len(height_map):
                    if height_maps[i_map][i_number + 1] < 9:
                        if [i_map, i_number + 1] not in points_to_explore:
                            points_to_explore.append([i_map, i_number + 1])
                            explored.append(False)

                if i_number > 0:
                    if height_maps[i_map][i_number - 1] < 9:
                        if [i_map, i_number - 1] not in points_to_explore:
                            points_to_explore.append([i_map, i_number - 1])
                            explored.append(False)

                # vertical neighbors
                if i_map + 1 < len(height_maps):
                    if height_maps[i_map + 1][i_number] < 9:
                        if [i_map + 1, i_number] not in points_to_explore:
                            points_to_explore.append([i_map + 1, i_number])
                            explored.append(False)

                if i_map > 0:
                    if height_maps[i_map - 1][i_number] < 9:
                        if [i_map - 1, i_number] not in points_to_explore:
                            points_to_explore.append([i_map - 1, i_number])
                            explored.append(False)

                explored[point] = True

            if size > min(basins):
                basins.remove(min(basins))
                basins.append(size)

    print(f"basins: {str(basins)}")
    print(f"score: {str(basins[0] * basins[1] * basins[2])}")


if __name__ == "__main__":
    day9_2()