def sentence_maker(pharase):
    cap = pharase.capitalize()
    introgativer = ("how","what","why")
    if pharase.startswith(introgativer):
        return "{}?".format(cap)
    else:
        return "{}".format(cap)

print(sentence_maker("what are you doing"))


