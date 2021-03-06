import fileinput


def pretty_print_list(arr):
    i = 0
    for a in arr:
        print(a, end=', ')
        i += 1
        if i % 15 == 0:
            print()
    if i % 15 != 0:
        print()


def lis_o2(A):
    # time complicity O(N^2) > O(N log N)?
    L = []
    for i in range(len(A)):
        # init max size of LIS
        max_l = 0
        for j in range(i):
            # check if can be appended
            if A[i] > A[j]:
                if L[j] > max_l:  # find longer LIS
                    # record size
                    max_l = L[j]
        L.append(max_l + 1)

    return max(L)


def lis(arr):
    """
    build program with 2 rules:
    1. same length, choose the smaller right edge
    2. same right edge, choose the longer sequence

    so, if we met a new number
    we try to append it to every element in the candidate list,
    if appendable, we copy the origin sequence,
    construct a new sequence with the new appended element,
    then we compare it with the exists candidate which has the same size.
    if the new list has a smaller right edge, we choose it.
    1. loop every right edge in the candidates
    2. if new element (n_e) is larger than the right edge of candidate i (c_i),
        we check the right edge of next candidate,
            if exists r_c_{i+k} (right edge of candidate i),
            if r_c_{i+k} < n_e:
                drop the new sequence
       so, we only append the new element to the last candidate,
       unless there exists a right edge in candidate, so that
       the right edge is larger than the new element.
       While we should consider the appendable problem.

    :param arr:
    :return:
    """
    N = len(arr)
    # cand_list = [[]]
    cand_end_list = [-1]
    for i in range(N):
        curr_num = arr[i]
        for j in range(len(cand_end_list)):
            ce = cand_end_list[j]
            if curr_num > ce:
                # check if has next_cand,
                # if has next_cand, compare right_edge
                if j+1 < len(cand_end_list):
                    next_cand = cand_end_list[j+1]
                    n_ce = next_cand
                    # if is a better choice, substitute
                    if curr_num < n_ce:
                        new_next_ce = curr_num
                        cand_end_list[j+1] = new_next_ce
                else:
                    # else append new_next_cand to cand_list
                    new_next_ce = curr_num
                    cand_end_list.append(new_next_ce)

    # pretty_print_list(arr)
    # print("longest lis:")
    # pretty_print_list(cand_list[-1])
    # first result is empty
    return len(cand_end_list) - 1


def lis_err(arr):
    """
    lis(i) = max(
        lis(i-1), with no condition
        lis(i-1) + 1, if arr[i] < lis_min[i-1]
    )
    prefer lis(i-1) over lis(i-1) + 1
    (because lis_min[i] will be larger,
    so it will cover more conditions)

    :param arr:
    :return:
    """
    max_size_of_is = 0


    print()
    for pos in range(len(arr)):
        print("starting pos", pos)
        prev_num = arr[pos]
        size_of_is = 1
        for curr_num in arr[pos:]:
            if curr_num > prev_num:
                print(curr_num, end=' ')
                size_of_is += 1
                prev_num = curr_num

        print()

        if size_of_is > max_size_of_is:
            max_size_of_is = size_of_is

    return max_size_of_is


def main2():
    f = fileinput.input()
    test_case_num = int(f.readline().strip())
    for i in range(test_case_num):
        size_of_arr = int(f.readline())
        arr = [int(x) for x in f.readline().strip().split()]
        print(lis(arr))


def main():
    with open("./input.txt") as f:
        test_case_num = int(f.readline().strip())
        for i in range(test_case_num):
            size_of_arr = int(f.readline())
            arr = [int(x) for x in f.readline().strip().split()]
            print(lis(arr))


if __name__ == "__main__":
    main()

