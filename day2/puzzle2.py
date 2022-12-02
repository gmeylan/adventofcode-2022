def get_file_content():
    f = open("input1.txt", "r")
    lines = [line.rstrip() for line in f.readlines()]
    f.close()
    return lines


if __name__ == "__main__":
    lines = get_file_content()
    # A for rock, B for paper, C for scissors
    # X for lose, Y for draw, Z for win
    # 1 for rock, 2 for paper, 3 for scissors
    # 0 lost, 3 draw, 6 won
    points = 0
    for l in lines:
        round = l.split()
        if round[0] == "A":
            if round[1] == "X":
                points += 0 + 3
            if round[1] == "Y":
                points += 3 + 1
            if round[1] == "Z":
                points += 6 + 2
        if round[0] == "B":
            if round[1] == "X":
                points += 0 + 1
            if round[1] == "Y":
                points += 3 + 2
            if round[1] == "Z":
                points += 6 + 3
        if round[0] == "C":
            if round[1] == "X":
                points += 0 + 2
            if round[1] == "Y":
                points += 3 + 3
            if round[1] == "Z":
                points += 6 + 1

    print(points)
