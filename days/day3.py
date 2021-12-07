from copy import deepcopy

def day3():
    with open("../resources/day3.txt") as file:
        lines = file.readlines()

    total_lines = len(lines)
    count_1s = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for line in lines:
        bits = list(line.rstrip())

        for idx, bit in enumerate(bits):
            if int(bit):
                count_1s[idx] += 1

    gamma_rate_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    epsilon_rate_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for idx, count in enumerate(count_1s):
        if count * 2 > total_lines:
            gamma_rate_list[idx] = 1
        else:
            epsilon_rate_list[idx] = 1

    gamma_rate = ''.join(str(e) for e in gamma_rate_list)
    epsilon_rate = ''.join(str(e) for e in epsilon_rate_list)

    gam_dec = int(gamma_rate, 2)
    eps_dec = int(epsilon_rate, 2)

    print(gam_dec)
    print(eps_dec)

    print(gam_dec * eps_dec)

def day3_2():
    with open("../resources/day3.txt") as file:
        lines = file.readlines()

    count_1s = [[], [], [], [], [], [], [], [], [], [], [], []]
    count_0s = [[], [], [], [], [], [], [], [], [], [], [], []]

    bits_indexes = list()


    for line_index, line in enumerate(lines):
        bits = list(line.rstrip())

        bits_indexes.append(line_index)

        for bit_index, bit in enumerate(bits):
            if int(bit):
                count_1s[bit_index].append(line_index)
            else:
                count_0s[bit_index].append(line_index)

    oxygen_generator_rating_indexes = deepcopy(bits_indexes)
    count_1s_oxygen = deepcopy(count_1s)
    count_0s_oxygen = deepcopy(count_0s)

    co2_scrubber_indexes = deepcopy(bits_indexes)
    count_1s_co2 = deepcopy(count_1s)
    count_0s_co2 = deepcopy(count_0s)


    for count in range (0, 12):
        if len(count_1s_oxygen[count]) * 2 >= len(oxygen_generator_rating_indexes):
            oxygen_generator_rating_indexes = deepcopy(count_1s_oxygen[count])
        else:
            oxygen_generator_rating_indexes = deepcopy(count_0s_oxygen[count])

        for count2 in range(count + 1, 12):
            count_1s_oxygen[count2] = list(set(count_1s_oxygen[count2]).intersection(set(oxygen_generator_rating_indexes)))
            count_0s_oxygen[count2] = list(set(count_0s_oxygen[count2]).intersection(set(oxygen_generator_rating_indexes)))

        if len(oxygen_generator_rating_indexes) == 1:
            break

    for count in range(0, 12):
        if len(count_0s_co2[count]) * 2 <= len(co2_scrubber_indexes):
            co2_scrubber_indexes = deepcopy(count_0s_co2[count])
        else:
            co2_scrubber_indexes = deepcopy(count_1s_co2[count])

        for count2 in range(count + 1, 12):
            count_1s_co2[count2] = list(set(count_1s_co2[count2]).intersection(set(co2_scrubber_indexes)))
            count_0s_co2[count2] = list(set(count_0s_co2[count2]).intersection(set(co2_scrubber_indexes)))

        if len(co2_scrubber_indexes) == 1:
            break

    print(f" oxygen generator number: {lines[oxygen_generator_rating_indexes[0]]}")
    print(f"co2 generator number: {lines[co2_scrubber_indexes[0]]}")

    ox_dec = int(lines[oxygen_generator_rating_indexes[0]], 2)
    co2_dec = int(lines[co2_scrubber_indexes[0]], 2)


    print(ox_dec * co2_dec)



if __name__ == "__main__":
    day3_2()
