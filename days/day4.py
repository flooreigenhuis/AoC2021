def day4():
    with open("../resources/day4.txt") as f:
        lines = f.readlines()

    # lines = lines.split("\n\n")

    input = lines.pop(0)

    bingo_cards = []

    bingo_card = []

    called = []

    for line in lines:
        if line == "\n":
            if bingo_card:
                bingo_cards.append(bingo_card)

                called.append([[False, False, False, False, False],
                               [False, False, False, False, False],
                               [False, False, False, False, False],
                               [False, False, False, False, False],
                               [False, False, False, False, False]])
            bingo_card = []
        else:
            line = line.replace('\n', '')
            row_list = []
            for number in (line.split(" ")):
                if not number == "\n" and number:
                    row_list.append(int(number))
            bingo_card.append(row_list)

    found = False

    for number in input.split(","):
        if found:
            break
        for bingo_idx, bingo_card in enumerate(bingo_cards):
            for line_idx, line in enumerate(bingo_card):
                for value_idx, value in enumerate(line):
                    if value == int(number):
                        called[bingo_idx][line_idx][value_idx] = True

                if found:
                    break
                for line in called[bingo_idx]:
                    if True in line and len(set(line)) == 1:
                        print(f"FOUND WINNING BINGO horizontal {str(called[bingo_idx])}")
                        print(f"card: {str(bingo_cards[bingo_idx])}, number {number}")
                        score = get_score(called, bingo_cards, bingo_idx, number)

                        print(f"score {score}")
                        found = True
                        break

                # vertical
                line = called[bingo_idx][0]
                for value_idx, value in enumerate(line):
                    if value:
                        if (called[bingo_idx][1][value_idx] and
                                   called[bingo_idx][2][value_idx] and
                                   called[bingo_idx][3][value_idx]  and
                                called[bingo_idx][4][value_idx] ):
                            print(f"FOUND WINNING BINGO vertical "
                                  f"{str(called[bingo_idx])}")
                            score = get_score(called, bingo_cards, bingo_idx,
                                              number)

                            print(f"score {score}")

                            found = True
                            break

def day4_2():
    with open("../resources/day4.txt") as f:
        lines = f.readlines()

    # lines = lines.split("\n\n")

    input = lines.pop(0)

    bingo_cards = []

    bingo_card = []

    called = []


    for line in lines:
        if line == "\n":
            if bingo_card:
                bingo_cards.append(bingo_card)

                called.append([[False, False, False, False, False],[False, False, False, False, False],[False, False, False, False, False],[False, False, False, False, False],[False, False, False, False, False]])
            bingo_card = []
        else:
            line = line.replace('\n', '')
            row_list = []
            for number in (line.split(" ")):
                if not number == "\n" and number:
                    row_list.append(int(number))
            bingo_card.append(row_list)

    won = [False] * len(bingo_cards)

    found = False

    for number in input.split(","):
        if found:
            break
        for bingo_idx, bingo_card in enumerate(bingo_cards):
            for line_idx, line in enumerate(bingo_card):
                for value_idx, value in enumerate(line):
                    if value == int(number):
                        called[bingo_idx][line_idx][value_idx] = True

            if not won[bingo_idx]:
                for line in called[bingo_idx]:
                    if True in line and len(set(line)) == 1:
                        if won.count(False) == 1:
                            idx = won.index(False)
                            score = get_score(called, bingo_cards, idx,
                                              number)
                            print(score)
                            found = True
                            break
                        else:
                            won[bingo_idx] = True
                        break

                # vertical
                line = called[bingo_idx][0]
                for value_idx, value in enumerate(line):
                    if value:
                        if (called[bingo_idx][1][value_idx] and
                                called[bingo_idx][2][value_idx] and
                                called[bingo_idx][3][value_idx]  and called[bingo_idx][4][value_idx] ):
                            if won.count(False) == 1:
                                idx = won.index(False)
                                score = get_score(called, bingo_cards, idx,
                                                  number)
                                print(score)
                                found = True
                                break
                            else:
                                won[bingo_idx] = True
                            break


def get_score(called, bingo_cards, bingo_idx, number):
    sum = 0
    for line_idx, called_line in enumerate(called[bingo_idx]):
        for value_idx, called_value in enumerate(called_line):
            if not called_value:
                sum+=bingo_cards[bingo_idx][line_idx][value_idx]

    return sum * int(number)


if __name__ == "__main__":
    day4_2()
