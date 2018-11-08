def lcs(s1, s2):
    return


def main(input_file):
    with open(input_file) as f:
        test_case_num = int(f.readline().strip())
        for i in range(test_case_num):
            (s1_l, s2_l) = [int(x) for x in f.readline().strip().split(" ")]
            s1 = f.readline().strip()
            s2 = f.readline().strip()
            print(lcs(s1, s2))


if __name__ == "__main__":
    in_file = "./input.txt"
    main(in_file)