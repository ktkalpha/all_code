import random
def encryption(s):
    return_list = []
    for x in range(len(s)):
        return_list.append(s[x])
        return_list.append(str(random.randint(0, 9)))
    random.shuffle(return_list)
    n = "".join(return_list)
    return n
