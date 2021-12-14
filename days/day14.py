import copy
from collections import Counter
import time


def day14():
    with open("../resources/day14.txt") as f:
        lines = f.read().splitlines()

    insertion_dict = {}
    for line in lines:
        split = line.split("->")
        insertion_dict[split[0].strip()] = split[1].strip()

    input = list("SHHBNFBCKNHCNOSHHVFF")

    for _ in range(0, 10):
        new_input = []
        for i in range(1, len(input)):
            key = ''.join(input[i - 1:i + 1])
            if key in insertion_dict.keys():
                # need to append first item to list
                if not new_input:
                    new_input.append(input[i - 1])
                new_input.extend([insertion_dict[key], input[i]])

        input = copy.deepcopy(new_input)

    counter = Counter(input)
    min_key = min(counter, key=counter.get)
    max_key = max(counter, key=counter.get)

    print(f"result: {counter[max_key] - counter[min_key]}")


def day14_2():
    start = time.time()
    with open("../resources/day14.txt") as f:
        lines = f.read().splitlines()

    insertion_dict = {}
    counter_dict = {}
    for line in lines:
        split = line.split("->")
        insertion_dict[split[0].strip()] = split[1].strip()
        counter_dict[split[0].strip()] = 0

    input = list("SHHBNFBCKNHCNOSHHVFF")
    # input = list("NNCB")
    last_letter = "F"

    # start dict iteration
    for i in range(1, len(input)):
        key = ''.join(input[i - 1:i + 1])
        if key in insertion_dict.keys():
            counter_dict[key] += 1

    temp_counter_dict = copy.deepcopy(counter_dict)
    for _ in range(1, 40):
        for key, value in insertion_dict.items():
            if counter_dict[key] > 0:
                key1 = key[0] + value
                key2 = value + key[1]

                temp_counter_dict[key1] += counter_dict[key]
                temp_counter_dict[key2] += counter_dict[key]
                temp_counter_dict[key] -= counter_dict[key]
        counter_dict = copy.deepcopy(temp_counter_dict)

    counter = {}
    for key, value in insertion_dict.items():
        occurences = counter_dict[key]

        for letter in [key[0], value]:
            if letter in counter.keys():
                counter[letter] += occurences
            else:
                counter[letter] = occurences

    counter[last_letter] += 1

    min_key = min(counter, key=counter.get)
    max_key = max(counter, key=counter.get)

    print(f"result: {counter[max_key] - counter[min_key]}")

    end = time.time()

    print(f"elapsed time: {end-start} seconds")


if __name__ == "__main__":
    day14_2()
