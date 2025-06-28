s = "({)"

sample = []

diction = {
    "}" : "{",
    "]" : "[",
    ")" : "("
}
def valid1(s):
    for x in s:
        if x in "{[(":
            sample.append(x)
        else:
            if not sample:
                return False
            if x not in diction:
                return False
            if sample.pop() != diction[x]:
                return False

    return len(sample) == 0

print(valid1(s))