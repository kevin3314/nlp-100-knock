import gzip
import json
import pprint
import re

JSON_PATH = "jawiki-country.json.gz"


def problem_20():
    with gzip.open(JSON_PATH, "rt") as f:
        for line in f:
            js = json.loads(line)
            if js["title"] == "イギリス":
                return js["text"]


def problem_21():
    text = problem_20()
    pattern = re.compile(r"^.*\[\[Category:.*\]\].*$", re.MULTILINE)
    result = pattern.findall(text)

    # 結果表示
    for line in result:
        print(line)


def problem_22():
    text = problem_20()
    pattern = re.compile(r"^.*\[\[Category:(.*?)(?:\|.*)?\]\].*$", re.MULTILINE)
    result = pattern.findall(text)

    # 結果表示
    for line in result:
        print(line)


def problem_23():
    text = problem_20()
    pattern = re.compile(
        r"^(={2,})\s*(.+?)\s*\1.*$",
        re.MULTILINE
    )

    result = pattern.findall(text)

    # 結果表示
    for line in result:
        level = len(line[0]) - 1
        print(f"{line[1]} -> {level}")


def problem_24():
    text = problem_20()
    pattern = re.compile(
        r"\[\[(?:[^]^[]*?):([^]]*?)\|(?:[^]]*?)\|(?:[^]]*)\]\]",
        re.MULTILINE
    )

    result = pattern.findall(text)

    for line in result:
        print(line)


def problem_25():
    text = problem_20()
    # what should I extract??


def problem_26():
    text = problem_20()
    pattern = re.compile(
        r"^(.*?)('''''|'''|'')(.*?)(\2)(.*?)",
        re.MULTILINE
    )

    result = pattern.findall(text)

    for line in result:
        print(f"{line[0]}{line[2]}{line[4]}")

print(problem_26())
