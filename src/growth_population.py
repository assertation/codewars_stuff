def nb_year(p0, percent, aug, p, depth=1):
    total = p0 + int(p0 * percent / 100) + aug
    return depth if total >= p else nb_year(total, percent, aug, p, depth+1)
