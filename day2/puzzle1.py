def get_file_content():
    f = open("input1.txt", "r")
    lines = [line.rstrip() for line in f.readlines()]
    f.close()
    return lines


if __name__ == "__main__":
    lines = get_file_content()
    # A for rock, B for paper, C for scissors
    # X for rock, Y for paper, Z for scissors
    # 1 for rock, 2 for paper, 3 for scissors
    # 0 lost, 3 draw, 6 won
    points = 0
    for l in lines:
        round = l.split()
        if round[0] == "A":
            if round[1] == "X":
                points += 1 + 3
            if round[1] == "Y":
                points += 2 + 6
            if round[1] == "Z":
                points += 3 + 0
        if round[0] == "B":
            if round[1] == "X":
                points += 1 + 0
            if round[1] == "Y":
                points += 2 + 3
            if round[1] == "Z":
                points += 3 + 6
        if round[0] == "C":
            if round[1] == "X":
                points += 1 + 6
            if round[1] == "Y":
                points += 2 + 0
            if round[1] == "Z":
                points += 3 + 3

    print(points)
