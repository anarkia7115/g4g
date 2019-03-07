<<<<<<< HEAD
def lcs(s1, s2):
    """
    a) use a row to record longest 
        match sequence (match_seq, idx:i)
    b) if e_i == e_j, new_m += m[j-1, i-1] + 1
       elif new_m = max(m[j-1, i], m[i, j-1])
    c) return m[max_i]
    the longest common sequence of (s1, s2)
    :param s1:
    :param s2:
    :return:
    """
    # a) use a row to record longest 
    #     match sequence (match_seq, idx:i)
    m = [0] * len(s1)
    om = m[:]  # old m
    # s1: i, m: i
    # s2: j
    # print(s1, s2)
    # print("      ", "  ".join(list(s1)))
    for j in range(len(s2)):
        e_j = s2[j]
        for i in range(len(s1)):
            e_i = s1[i]
            # b) if e_i == e_j, m[i] += 1
            # b) if e_i == e_j, new_m += m[j-1, i-1]
            if e_i == e_j:
                """
                if e_i is the first element, m[i] should <= 1
                if e_i-1 exists, m[i] +=1 only if m[i-1] == m[i]
                """
                if i == 0:
                    m[i] = 1
                else:
                    m[i] = om[i-1] + 1
            # elif new_m = max(m[j-1, i], m[j, i-1])
            else:
                if i == 0:
                    m[i] = om[i]
                else:
                    m[i] = max(om[i], m[i-1])
        # goto next row
        om = m[:]

        # print("m[{}]: {}".format(e_j, m))
    return m[len(s1) - 1]


def main2():
    import fileinput
    f = fileinput.input()
    test_case_num = int(f.readline().strip())
    for _ in range(test_case_num):
        (_, _) = [int(x) for x in f.readline().strip().split(" ")]
        s1 = f.readline().strip()
        s2 = f.readline().strip()
        # print(s1, s2, lcs(s1, s2))
        print(lcs(s1, s2))

def main(input_file):
    with open(input_file) as f:
        test_case_num = int(f.readline().strip())
        for _ in range(test_case_num):
            (_, _) = [int(x) for x in f.readline().strip().split(" ")]
            s1 = f.readline().strip()
            s2 = f.readline().strip()
            # print(s1, s2, lcs(s1, s2))
            print(lcs(s1, s2))


if __name__ == "__main__":
    in_file = "./input.txt"
    main(in_file)
=======
def lcs(s1, s2):
    """
    a) use a row to record longest 
        match sequence (match_seq, idx:i)
    b) if e_i == e_j, new_m += m[j-1, i-1] + 1
       elif new_m = max(m[j-1, i], m[i, j-1])
    c) return m[max_i]
    the longest common sequence of (s1, s2)
    :param s1:
    :param s2:
    :return:
    """
    # a) use a row to record longest 
    #     match sequence (match_seq, idx:i)
    m = [0] * len(s1)
    om = m[:]  # old m
    # s1: i, m: i
    # s2: j
    # print(s1, s2)
    # print("      ", "  ".join(list(s1)))
    for j in range(len(s2)):
        e_j = s2[j]
        for i in range(len(s1)):
            e_i = s1[i]
            # b) if e_i == e_j, m[i] += 1
            # b) if e_i == e_j, new_m += m[j-1, i-1]
            if e_i == e_j:
                """
                if e_i is the first element, m[i] should <= 1
                if e_i-1 exists, m[i] +=1 only if m[i-1] == m[i]
                """
                if i == 0:
                    m[i] = 1
                else:
                    m[i] = om[i-1] + 1
            # elif new_m = max(m[j-1, i], m[j, i-1])
            else:
                if i == 0:
                    m[i] = om[i]
                else:
                    m[i] = max(om[i], m[i-1])
        # goto next row
        om = m[:]

        # print("m[{}]: {}".format(e_j, m))
    return m[len(s1) - 1]


def main2():
    import fileinput
    f = fileinput.input()
    test_case_num = int(f.readline().strip())
    for _ in range(test_case_num):
        (_, _) = [int(x) for x in f.readline().strip().split(" ")]
        s1 = f.readline().strip()
        s2 = f.readline().strip()
        # print(s1, s2, lcs(s1, s2))
        print(lcs(s1, s2))

def main(input_file):
    with open(input_file) as f:
        test_case_num = int(f.readline().strip())
        for _ in range(test_case_num):
            (_, _) = [int(x) for x in f.readline().strip().split(" ")]
            s1 = f.readline().strip()
            s2 = f.readline().strip()
            # print(s1, s2, lcs(s1, s2))
            print(lcs(s1, s2))


if __name__ == "__main__":
    in_file = "./input.txt"
    main(in_file)
>>>>>>> 8166ec0029f8c47d05ede1a36a885154592508fb
