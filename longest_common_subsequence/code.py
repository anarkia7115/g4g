def lcs(s1, s2):
    """
    the longest common sequence of (s1, s2)
    the longest common sequence of (s1[1:], s2)
    :param s1:
    :param s2:
    :return:
    """
    s2_start = 0
    common_size = 0
    common_str = ""
    for i in range(len(s1)):
        ch1 = s1[i]
        for j in range(s2_start, len(s2)):
            ch2 = s2[j]
            # check if ch1, ch2 is equal
            # if equal continue to next char of s1
            # begin from next char in s2
            # else do nothing
            if ch1 == ch2:
                s2_start = j + 1
                common_size += 1
                common_str += ch1
                break

    return common_size, common_str


def main(input_file):
    with open(input_file) as f:
        test_case_num = int(f.readline().strip())
        for i in range(test_case_num):
            (s1_l, s2_l) = [int(x) for x in f.readline().strip().split(" ")]
            s1 = f.readline().strip()
            s2 = f.readline().strip()
            print(s1, s2, lcs(s1, s2))


if __name__ == "__main__":
    in_file = "./input.txt"
    main(in_file)