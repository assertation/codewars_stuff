move_zeros = lambda x: list(filter(int(0).__ne__, x)) + [0] * sum(map(lambda y: y == 0, x))
