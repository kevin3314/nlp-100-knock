from collections import defaultdict, Counter
import matplotlib.pyplot as plt
import numpy as np
from math import log
import japanize_matplotlib


def neco_parse():
    with open('./neko.txt.mecab') as f:
        morphems = []

        while 1:
            token = f.readline()
            if not token:
                break

            if "EOS" in token:
                if morphems:
                    yield morphems
                morphems = []

            dic = {}
            splitted = token.split("\t")
            if len(splitted) < 2:
                continue

            res = splitted[1].split(",")
            dic["surface"] = splitted[0]
            dic["base"] = res[-3]
            dic["pos"] = res[0]
            dic["pos1"] = res[1]
            morphems.append(dic)
            if "。" in token:
                if morphems:
                    yield morphems
                morphems = []



def problem_31():
    res_set = set()
    for morphems in neco_parse():
        for morphem in morphems:
            if morphem["pos"] == "動詞":
                res_set.add(morphem["surface"])
    print(res_set)


def problem_32():
    res_set = set()
    for morphems in neco_parse():
        for morphem in morphems:
            if morphem["pos"] == "動詞":
                res_set.add(morphem["base"])
    print(res_set)


def problem_33():
    for morphems in neco_parse():
        for i in range(1, len(morphems)-1):
            if morphems[i-1]["pos"] != "名詞" or morphems[i+1]["pos"] != "名詞":
                continue
            A_n = morphems[i-1]["surface"]
            no = morphems[i]["surface"]
            B_n = morphems[i+1]["surface"]
            if no == "の":
                print(f"{A_n} - {B_n}")


def problem_34():
    for morphems in neco_parse():
        i, j = 0, 0
        while 1:
            if i >= len(morphems):
                break
            if morphems[i]["pos"] == "名詞":
                j += 1
                while 1:
                    if j == len(morphems):
                        j -= 1
                        break
                    if morphems[j]["pos"] == "名詞":
                        j += 1
                    else:
                        j -= 1
                        break
                if i != j:
                    norms = [x["surface"] for x in morphems[i:j+1]]
                    print(",".join(x["surface"] for x in morphems[i:j+1]))
                i = j
                i += 1
                j += 1
            else:
                i += 1
                j += 1


def problem_35():
    tmp = []
    for morphems in neco_parse():
        norms = [x["surface"] for x in morphems]
        tmp += norms
    co = Counter(tmp)
    return co


def problem_36():
    co = problem_35()
    top_10 = co.most_common(10)
    keys = [x[0] for x in top_10]
    values = [x[1] for x in top_10]
    left = np.arange(10)
    plt.bar(left, values, tick_label=keys)
    plt.show()


def problem_37():
    dic = defaultdict(int)
    for morphems in neco_parse():
        words = [x["surface"] for x in morphems]
        if "猫" in words:
            for word in words:
                if word != "猫":
                    dic[word] += 1

    count = []
    for key, value in dic.items():
        count.append((key, value))
    count.sort(key=lambda x: x[1], reverse=True)
    top_10 = count[:10]
    keys = [x[0] for x in top_10]
    values = [x[1] for x in top_10]
    left = np.arange(10)
    plt.bar(left, values, tick_label=keys)
    plt.show()


def problem_38():
    co = problem_35()

    all_score = [i[1] for i in sorted(co.items(), key=lambda x: -x[1])]
    plt.hist(all_score, range(10, 100))
    plt.show()


def problem_39():
    co = problem_35()
    log_idx = [log(i + 1) for i in range(len(co.values()))]
    log_all_score = [log(i[1]) for i in sorted(co.items(), key=lambda x: -x[1])]
    plt.scatter(log_idx, log_all_score)
    plt.show()
