def get_file_content():
    f = open("input1.txt", "r")
    lines = [line.rstrip() for line in f.readlines()]
    f.close()
    return lines


if __name__ == "__main__":
    values = {}
    for i in range(1, 27):
        values[chr(i -1 + 97)] = i
    for i in range(0, 26):
        values[chr(i + 65)] = 26 + i + 1
    lines = get_file_content()
    solutions = []
    for l in lines:
        length = len(l)//2
        s1 = l[:length]
        s2 = l[length:]
        for i in range(length):
            if(s1[i] in s2):
                solutions.append(s1[i])
                break
    sum_priority = 0
    for s in solutions:
        sum_priority += values[s]
    #     # print(ord(s))
    print(sum_priority)