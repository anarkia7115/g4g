def greedy(W, val, wt):
    for i in range(len(val)-1, 0, -1):
    pass


def main2():
    import fileinput
    f = fileinput.input()
    test_case_num = int(f.readline().strip())
    for _ in range(test_case_num):
        # (_, _) = [int(x) for x in f.readline().strip().split(" ")]
        _ = int(f.readline().strip())
        W = int(f.readline().strip())
        val = [int(x) for x in f.readline().strip().split(" ")]
        wt = [int(x) for x in f.readline().strip().split(" ")]
        # print(s1, s2, lcs(s1, s2))
        print(greedy(W, val, wt))

def main(input_file):
    with open(input_file) as f:
        test_case_num = int(f.readline().strip())
        for _ in range(test_case_num):
            # (_, _) = [int(x) for x in f.readline().strip().split(" ")]
            _ = int(f.readline().strip())
            W = int(f.readline().strip())
            val = [int(x) for x in f.readline().strip().split(" ")]
            wt = [int(x) for x in f.readline().strip().split(" ")]
            # print(s1, s2, lcs(s1, s2))
            print(greedy(W, val, wt))


if __name__ == "__main__":
    in_file = ".\\longest_common_subsequence\\input.txt"
    main(in_file)