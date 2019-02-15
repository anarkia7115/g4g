def emphasis_i(s1, i):
    if i+1 < len(s1):
        return s1[:i]+'['+s1[i]+']'+s1[i+1:]
    else:
        return s1 + "[]"


dis_table = dict()


def edit_dis(s1, s2, moves=0, i=0, forward=0):
    # print("comparing: ", emphasis_i(s1, i), emphasis_i(s2, i))
    # final condition
    if s1 == s2:
        return moves

    # read from mem
    if forward in dis_table and i in dis_table[forward]:
        return dis_table[forward][i]

    # check bound
    if i >= len(s1) and len(s1) < len(s2):
        # delete longer
        s2 = s2[:-1]
        moves += 1
        return edit_dis(s1, s2, moves, i, forward)
    if i >= len(s2) and len(s2) < len(s1):
        s1 = s1[:-1]
        moves += 1
        return edit_dis(s1, s2, moves, i, forward)

    c1 = s1[i]
    c2 = s2[i]

    # all 4 distance
    # if same char, pass
    if c1 == c2:  # no move
        dis_n = edit_dis(s1, s2, moves, i+1, forward)
        return dis_n
    else:  # 3 moves
        # s1 insert <=> s2 delete
        # insert
        # print("insert")
        dis_i = edit_dis(s1[:i]+s2[i]+s1[i:], s2, moves+1, i+1, forward)
        # delete
        # print("delete")
        dis_d = edit_dis(s1[:i]+s1[i+1:], s2, moves+1, i, forward)
        # replace
        # print("replace")
        dis_r = edit_dis(s1[:i]+s2[i]+s1[i+1:], s2, moves+1, i+1, forward)

        # compare distance
        dis_return = 0
        if dis_i <= dis_d and dis_i <= dis_r:
            forward += 1
            dis_return = dis_i
        elif dis_d <= dis_i and dis_d <= dis_r:
            forward -= 1
            dis_return = dis_d
        elif dis_r <= dis_i and dis_r <= dis_d:
            dis_return = dis_r

        if forward not in dis_table:
            dis_table[forward] = dict()
        dis_table[forward][i] = dis_return

        return dis_return


def main(f):
    test_case_num = int(f.readline().strip())
    for _ in range(test_case_num):
        f.readline() # skip one line
        s1, s2 = f.readline().strip().split()
        # print(s1, s2, lcs(s1, s2))
        print(edit_dis(s1, s2))


if __name__ == "__main__":
    # import fileinput
    # f = fileinput.input()
    # main(f)

    input_file = "./input.txt"
    with open(input_file, 'r') as f:
        main(f)
