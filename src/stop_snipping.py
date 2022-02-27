def spin_words(sentence):
    parts = sentence.split()
    if len(parts) > 1:
        return " ".join(list(map(lambda x: spin_words(x), parts)))
    return sentence if len(sentence) < 5 else sentence[::-1]
