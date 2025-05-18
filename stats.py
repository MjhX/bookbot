def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    letter_dict = {}
    for c in text:
        cl = c.lower()
        letter_dict.setdefault(cl,0)
        letter_dict[cl] += 1
    return letter_dict

def get_sorted_chars(dict):
    ret = []
    for k,v in dict.items():
        ret.append({"char": k, "num": v})
    ret.sort(reverse=True,key=lambda d:d["num"])
    return ret
    