def emphasis_i(s1, i):
    if i+1 < len(s1):
        return s1[:i]+'['+s1[i]+']'+s1[i+1:]
    else:
        return s1 + "[]"


def edit_dis(s1, s2, moves=0, i=0):
    # print("comparing: ", emphasis_i(s1, i), emphasis_i(s2, i))
    # final condition
    if s1 == s2:
        return moves

    # check bound
    if i >= len(s1) and len(s1) < len(s2):
        # delete longer
        s2 = s2[:-1]
        moves += 1
        return edit_dis(s1, s2, moves, i)
    if i >= len(s2) and len(s2) < len(s1):
        s1 = s1[:-1]
        moves += 1
        return edit_dis(s1, s2, moves, i)

    c1 = s1[i]
    c2 = s2[i]

    # all 4 distance
    # if same char, pass
    if c1 == c2:  # no move
        dis_n = edit_dis(s1, s2, moves, i+1)
        return dis_n
    else:  # 3 moves
        # s1 insert <=> s2 delete
        # insert
        # print("insert")
        dis_i = edit_dis(s1[:i]+s2[i]+s1[i:], s2, moves+1, i+1)
        # delete
        # print("delete")
        dis_d = edit_dis(s1[:i]+s1[i+1:], s2, moves+1, i)
        # replace
        # print("replace")
        dis_r = edit_dis(s1[:i]+s2[i]+s1[i+1:], s2, moves+1, i+1)

        # compare distance
        if dis_i <= dis_d and dis_i <= dis_r:
            return dis_i
        elif dis_d <= dis_i and dis_d <= dis_r:
            return dis_d
        elif dis_r <= dis_i and dis_r <= dis_d:
            return dis_r


def main(f):
    test_case_num = int(f.readline().strip())
    for _ in range(test_case_num):
        f.readline() # skip one line
        s1, s2 = f.readline().strip().split()
        # print(s1, s2, lcs(s1, s2))
        # print(edit_dis(s1, s2))


if __name__ == "__main__":
    import fileinput
    f = fileinput.input()
    main(f)

    # input_file = "./input.txt"
    # with open(input_file, 'r') as f:
    #     main(f)
