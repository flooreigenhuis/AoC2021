import statistics

def day10():
    with open("../resources/day10.txt") as f:
        lines = f.readlines()

    score = 0
    for line in lines:
        line = line.strip()

        char_list = []
        for character in line:
            match character:
                case "}":
                    if char_list[-1] == "{":
                        char_list.pop()
                        continue
                    score += get_score_1(character)
                    break
                case "]":
                    if char_list[-1] == "[":
                        char_list.pop()
                        continue
                    score += get_score_1(character)
                    break
                case ")":
                    if char_list[-1] == "(":
                        char_list.pop()
                        continue
                    score += get_score_1(character)
                    break
                case ">":
                    if char_list[-1] == "<":
                        char_list.pop()
                        continue
                    score += get_score_1(character)
                    break
                case _:
                    char_list.append(character)

    print(f"Score: {score}")

def day10_2():
    with open("../resources/day10.txt") as f:
        lines = f.readlines()

    scores = []
    for line in lines:
        score = 0
        line = line.strip()

        char_list = []
        incorrect = False
        for character in line:
            match character:
                case "}":
                    if char_list[-1] == "{":
                        char_list.pop()
                        continue
                    incorrect = True
                    break
                case "]":
                    if char_list[-1] == "[":
                        char_list.pop()
                        continue
                    incorrect = True
                    break
                case ")":
                    if char_list[-1] == "(":
                        char_list.pop()
                        continue
                    incorrect = True
                    break
                case ">":
                    if char_list[-1] == "<":
                        char_list.pop()
                        continue
                    incorrect = True
                    break
                case _:
                    char_list.append(character)

        if incorrect:
            continue

        for char in reversed(char_list):
            match char:
                case "{":
                    score = get_score_2("}", score)
                    continue
                case "[":
                    score = get_score_2("]", score)
                    continue
                case "(":
                    score = get_score_2(")", score)
                    continue
                case "<":
                    score = get_score_2(">", score)

        scores.append(score)

    final_score = statistics.median(scores)

    print(f"Final score: {final_score}")

def get_score_1(character):
    match character:
        case "}":
            return 1197
        case "]":
            return 57
        case ")":
            return 3
        case ">":
            return 25137

def get_score_2(character, score):
    score = score * 5
    match character:
        case "}":
            return score + 3
        case "]":
            return score + 2
        case ")":
            return score + 1
        case ">":
            return score + 4



if __name__ == "__main__":
    day10_2()
