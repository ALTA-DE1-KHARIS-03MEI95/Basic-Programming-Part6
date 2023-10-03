def find_max_sum_sub_array(k, arr):

    maks_sum = 0
    jumlah = 0
    for i in range(len(arr) - k + 1):
        jumlah = sum(arr[i:i+k])
        maks_sum = max(maks_sum, jumlah)
    return maks_sum

if __name__ == '__main__':
    print(find_max_sum_sub_array(3, [2, 1, 5, 1, 3, 2])) # 9
    print(find_max_sum_sub_array(2, [2, 3, 4, 1, 5])) # 7
    print(find_max_sum_sub_array(2, [2, 1, 4, 1, 1])) # 5
    print(find_max_sum_sub_array(3, [2, 1, 4, 1, 1])) # 7
    print(find_max_sum_sub_array(4, [2, 1, 4, 1, 1])) # 8