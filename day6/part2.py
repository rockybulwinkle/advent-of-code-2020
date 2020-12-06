import sys

letters = set("abcdefghijklmnopqrstuvwxyz")


def get_unique(group):
    answer = set(letters)
    for indiv in group:
        answer=answer.intersection(set(indiv))

    return answer


def load(fname):
    with open(fname, "r") as f:
        entries = [[]] #list of lists
        for line in f:
            line = line.strip()
            if not line:
                entries.append(list())
            else:
                entries[-1].append(line)

    retval = list()
    for line in entries:
        if line:
            retval.append(get_unique(line))

    return retval


if len(sys.argv) != 2:
    print("ya done did it wrong, boy")
    exit(-1)

answers = load(sys.argv[1])
count = 0
for answer in answers:
    print(answer)
    count += len(answer)

print(count)
