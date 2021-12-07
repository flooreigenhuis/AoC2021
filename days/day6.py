def day6():
    with open("../resources/day6.txt") as f:
        lines = f.read()

    initial_fish = lines.split(",")

    fishes_and_days = {}
    for fish in initial_fish:
        if int(fish) in fishes_and_days.keys():
            fishes_and_days[int(fish)] += 1
        else:
            fishes_and_days[int(fish)] = 1


    day = 1

    while day <= 256:
        temp_fish = {}
        for fish_days, fish_number in fishes_and_days.items():
            if fish_days > 0:
                if fish_days-1 in temp_fish.keys():
                    temp_fish[fish_days-1] += fish_number
                else:
                    temp_fish[fish_days-1] = fish_number
            else:
                if 6 in temp_fish.keys():
                    temp_fish[6] += fish_number
                else:
                    temp_fish[6] = fish_number
                temp_fish[8] = fish_number

        fishes_and_days = temp_fish.copy()
        day+=1

    print(sum(value for value in fishes_and_days.values()))

if __name__ == "__main__":
    day6()