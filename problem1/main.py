def compare(a, b):
    pattern = ""
    for i in range(len(a)):
        if i < len(b) and a[i] == b[i]:
            pattern += a[i]
        else:
            break
    return pattern
if __name__ == '__main__':
    print(compare("AKA", "AKASHI")) # AKA
    print(compare("KANGOORO", "KANG")) # KANG
    print(compare("KI", "KIJANG")) # KI
    print(compare("KUPU-KUPU", "KUPU")) # KUPU
    print(compare("ILALANG", "ILA")) # ILA