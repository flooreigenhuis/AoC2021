def day8():
    with open("../resources/day8.txt") as f:
        lines = f.readlines()

    outputs = []
    for line in lines:
        output = line.split("|")[1].replace("\n", "")

        outputs.extend(output.split(" "))

    count = 0
    for output in outputs:
        if len(output) == 2 or len(output) == 4 or len(output) == 3 or len(
                output) == 7:
            count += 1

    print(f"count: {count}")




def day8_2():
    with open("../resources/day8.txt") as f:
        lines = f.readlines()

    total_result = 0

    outputs = []
    inputs = []
    for line in lines:
        split_line = line.split("|")
        input = split_line[0].strip().replace("\n", "")
        output = split_line[1].strip().replace("\n", "")
        split_input = input.split(" ")
        split_input.sort(key=len)
        inputs.append(split_input)
        outputs.append(output.split(" "))

    for row_index, row in enumerate(inputs):

        # POSSIBLE POSITIONS:
        #       1111
        #      2    3
        #      2    3
        #       4444
        #      5    6
        #      5    6
        #       7777

        possible_letter_positions = {"a": "1234567", "b": "1234567",
                                     "c": "1234567",
                                     "d": "1234567", "e": "1234567",
                                     "f": "1234567",
                                     "g": "1234567"}
        # positions 3 and 6
        right_vertical = ""

        input_count = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0}
        # low-hanging fruit
        for input in row:
            # so it's a 1
            if len(input) == 2:
                filter_1s(input, possible_letter_positions)
                right_vertical = input

            # 7
            if len(input) == 3:
                filter_7s(input, possible_letter_positions)

            # 4
            if len(input) == 4:
                filter_4s(input, possible_letter_positions, right_vertical)

            # 0 or 6 or 9
            if len(input) == 6:
                for letter in right_vertical:
                    if letter not in input:
                        # it's a 6! letter must be position 3
                        filter_6s(letter, possible_letter_positions)

            for letter in input:
                input_count[letter] += 1

        # certain positions only appear in so many numbers
        for key, value in input_count.items():
            if value == 6:
                possible_letter_positions[key] = "2"
                remove_position_from_other_letters(key, "2", possible_letter_positions)

            if value == 4:
                possible_letter_positions[key] = "5"
                remove_position_from_other_letters(key, "5", possible_letter_positions)

        mappings = get_number_letter_mappings(possible_letter_positions)

        result = ""
        for output in outputs[row_index]:
            sorted_output = ''.join(sorted(output))
            result += str(mappings[sorted_output])

        total_result += int(result)

    print(int(total_result))


def filter_6s(letter, possible_letter_positions):
    possible_letter_positions[letter] = "3"
    remove_position_from_other_letters(letter, "3", possible_letter_positions)


def filter_4s(input, possible_letter_positions, right_vertical):
    remove_position_from_other_letters(input, "2",
                                       possible_letter_positions)
    remove_position_from_other_letters(input, "4",
                                       possible_letter_positions)
    for idx, letter in enumerate(input):
        if letter not in right_vertical:
            possible_letter_positions[letter] = "24"


def filter_7s(input, possible_letter_positions):
    for idx, letter in enumerate(input):
        if len(possible_letter_positions[letter]) > 2:
            possible_letter_positions[letter] = "1"

            remove_position_from_other_letters(letter, "1",
                                               possible_letter_positions)


def filter_1s(input, possible_letter_positions):
    remove_position_from_other_letters(input, "3",
                                       possible_letter_positions)
    remove_position_from_other_letters(input, "6",
                                       possible_letter_positions)
    for letter in input:
        possible_letter_positions[letter] = "36"


def get_number_letter_mappings(possible_letter_positions):
    mappings = {0: "", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "",
                9: ""}
    for key, value in possible_letter_positions.items():
        if value == "1":
            mappings[0] += key
            mappings[2] += key
            mappings[3] += key
            mappings[5] += key
            mappings[6] += key
            mappings[7] += key
            mappings[8] += key
            mappings[9] += key
        if value == "2":
            mappings[0] += key
            mappings[4] += key
            mappings[5] += key
            mappings[6] += key
            mappings[8] += key
            mappings[9] += key
        if value == "3":
            mappings[0] += key
            mappings[1] += key
            mappings[2] += key
            mappings[3] += key
            mappings[4] += key
            mappings[7] += key
            mappings[8] += key
            mappings[9] += key
        if value == "4":
            mappings[2] += key
            mappings[3] += key
            mappings[4] += key
            mappings[5] += key
            mappings[6] += key
            mappings[8] += key
            mappings[9] += key
        if value == "5":
            mappings[0] += key
            mappings[2] += key
            mappings[6] += key
            mappings[8] += key
        if value == "6":
            mappings[0] += key
            mappings[1] += key
            mappings[3] += key
            mappings[4] += key
            mappings[5] += key
            mappings[6] += key
            mappings[7] += key
            mappings[8] += key
            mappings[9] += key
        if value == "7":
            mappings[0] += key
            mappings[2] += key
            mappings[3] += key
            mappings[5] += key
            mappings[6] += key
            mappings[8] += key
            mappings[9] += key

    for key, value in mappings.items():
      mappings[key] = ''.join(sorted(value))

    mappings = {mappings[k]: k for k in mappings}

    return mappings


def remove_position_from_other_letters(letter, position, letter_dict):
    for key in letter_dict.keys():
        if key not in letter:
            letter_dict[key] = letter_dict[
                key].replace(position, "")


if __name__ == "__main__":
    day8_2()
