def problem_0():
    target = "stressed"
    return target[::-1]


def problem_1():
    target = "パタトクカシーー"
    return target[::2]


def problem_2():
    pat = "パトカー"
    tac = "タクシー"
    res = ""
    # maybe too naive(when len is not equal)
    for a, b in zip(pat, tac):
        res += a
        res += b
    return res


def problem_3():
    target = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    print(target[:-1])
    splitted = target[:-1].split()
    length_list = [len(x) for x in splitted]
    return length_list


def problem_4():
    target = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    shaped = target[:-1]
    splitted = shaped.split()
    rare_case = {0, 4, 5, 6, 7, 8, 14, 15, 18}
    result = {}
    for i, v in enumerate(splitted):
        if i in rare_case:
            key = v[0]
        else:
            key = v[:2]
        result[key] = i+1

    return result


def n_gram(s, n):
    return [s[idx:idx+n] for idx in range(len(s) - n + 1)]


def problem_6():
    a = "paraparaparadise"
    b = "paragraph"
    a_bi = set(n_gram(a, 2))
    b_bi = set(n_gram(b, 2))

    print(f"union -> {a_bi | b_bi}")
    print(f"intersection -> {a_bi & b_bi}")
    print(f"diff(a-b) -> {a_bi - b_bi}")

    print(f"se in X is -> {'se' in a_bi}")
    print(f"se in Y is -> {'se' in b_bi}")
