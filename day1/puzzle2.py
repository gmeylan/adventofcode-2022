def get_file_content():
    f = open("input1.txt", "r")
    lines = [line.rstrip() for line in f.readlines()]
    f.close()
    return lines


if __name__ == "__main__":
    lines = get_file_content()
    calories = 0
    max_calories = 0
    middle_calories = 0
    lowest_calories = 0
    for l in lines:
        if l == "":
            change_made = False
            if calories > max_calories and not change_made:
                lowest_calories = middle_calories
                middle_calories = max_calories
                max_calories = calories
                change_made = True
            if calories > middle_calories and not change_made:
                lowest_calories = middle_calories
                middle_calories = calories
                change_made = True
            if calories > lowest_calories and not change_made:
                lowest_calories = calories
                change_made = True
            calories = 0
        else:
            calories += int(l)

    print(lowest_calories + middle_calories + max_calories)
