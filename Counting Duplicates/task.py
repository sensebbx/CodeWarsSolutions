def duplicate_count(text):
    text = text.lower()
    res_dict = {}
    for i in text:
        if i not in res_dict:
            res_dict[i] = 1
            continue

        res_dict[i] += 1

    res_count = 0
    for i in res_dict.values():
        if i > 1:
            res_count += 1

    return res_count

