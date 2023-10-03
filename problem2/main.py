def caesar(offset, input_str):
    result = ""
    for teks in input_str:
        if teks.isalpha():
            ubah_ke_unicode = ord('A') if teks.isupper() else ord('a')
            ubah_ke_char = chr((ord(teks) - ubah_ke_unicode + offset) % 26 + ubah_ke_unicode)
            result += ubah_ke_char
        else:
            result += teks
    return result


if __name__ == '__main__':
    print(caesar(3, "abc")) # def
    print(caesar(2, "alta")) # cnvc
    print(caesar(10, "alterraacademy")) # kvdobbkkmknowi
    print(caesar(1, "abcdefghijklmnopqrstuvwxyz")) # bcdefghijklmnopqrstuvwxyza
    print(caesar(1000, "abcdefghijklmnopqrstuvwxyz")) # mnopqrstuvwxyzabcdefghijkl