def lis(arr):
    max_size_of_is = 0

    for pos in range(len(arr)):
        prev_num = arr[pos]
        size_of_is = 1
        for curr_num in arr[pos:]:
            if curr_num > prev_num:
                size_of_is += 1

        if size_of_is > max_size_of_is:
            max_size_of_is = size_of_is

    return max_size_of_is


def main(input_file):
    with open(input_file) as f:
        test_case_num = int(f.readline().strip())
        for i in range(test_case_num):
            size_of_arr = int(f.readline())
            arr = [int(x) for x in f.readline().strip().split()]
            print(lis(arr))


if __name__ == "__main__":
    main("./input.txt")

