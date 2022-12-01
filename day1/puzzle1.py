def get_file_content():
    f = open("input1.txt", "r")
    lines = [line.rstrip() for line in f.readlines()]
    f.close()
    return lines


if __name__ == "__main__":
    lines = get_file_content()
    calories = 0
    max_calories = 0
    for l in lines:
        if l == "":
            if calories > max_calories:
                max_calories = calories
            calories = 0
        else:
            calories += int(l)

    print(max_calories)
