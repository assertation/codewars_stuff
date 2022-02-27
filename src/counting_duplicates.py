def duplicate_count(text):
    sym = {}
    for x in text.lower():
        sym[x] = sym[x] + 1 if sym.get(x) else 1
    return sum(map(lambda x: x[1] > 1, sym.items()))
