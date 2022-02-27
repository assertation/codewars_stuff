def tribonacci(signature, n):
    i = len(signature)
    for x in range(i, n):
        signature.append(signature[i-1] + signature[i-2] + signature[i-3])
        i += 1
    return signature[:n]