from collections import Counter


def problem_10():
    with open("popular-names.txt") as f:
        lines = f.readlines()
    print(len(lines))


def problem_11():
    with open("popular-names.txt") as f:
        lines = f.readlines()
    lines = [v.replace("\t", " ") for v in lines]
    print(lines)


def problem_12():
    with open("popular-names.txt") as f:
        lines = f.readlines()
    col1 = []
    col2 = []
    for v in lines:
        splitted = v.split()
        col1.append(splitted[0])
        col2.append(splitted[1])

    with open("col1.txt", mode="w") as f:
        f.write("\n".join(col1))

    with open("col2.txt", mode="w") as f:
        f.write("\n".join(col2))


def problem_13():
    with open("col1.txt") as f:
        col1 = f.readlines()
    with open("col2.txt") as f:
        col2 = f.readlines()

    res = []
    for v1, v2 in zip(col1, col2):
        _v1 = v1.strip()
        _v2 = v2.strip()
        txt = f"{_v1}\t{_v2}"
        res.append(txt)

    with open("res.txt", mode="w") as f:
        f.write("\n".join(res))


def problem_14():
    n = int(input())
    with open("popular-names.txt") as f:
        lines = f.readlines()
    print(lines[:n])


def problem_15():
    n = int(input())
    with open("popular-names.txt") as f:
        lines = f.readlines()
    print(lines[-n:])


def problem_16():
    n = int(input())
    res = []
    with open("popular-names.txt") as f:
        lines = f.readlines()
    n_lines = len(lines)
    lines_per_group, mod = divmod(n_lines, n)
    if mod:
        lines_per_group += 1
    for i in range(n-1):
        res.append(lines[i*lines_per_group:(i+1)*lines_per_group])
    else:
        res.append(lines[(i+1)*lines_per_group:])


def problem_17():
    with open("popular-names.txt") as f:
        lines = f.readlines()
    col_1 = [v.split()[0] for v in lines]
    n = len(set(col_1))


def problem_18():
    def _get_key_number(s):
        splitted = s.split()
        return int(splitted[2])

    with open("popular-names.txt") as f:
        lines = f.readlines()
    lines.sort(key=_get_key_number, reverse=True)


def problem_19():
    with open("popular-names.txt") as f:
        lines = f.readlines()

    def _get_one_column(s):
        splitted = s.split()
        return splitted[0]
    one_columns = [_get_one_column(x) for x in lines]
    counter = Counter(one_columns)
    res = list(counter.keys())
    print(res)
