class PathInMatrix(object):
    def __init__(self, mat_dim):
        self.sum_table = [[-1] * mat_dim] * mat_dim

    def max_val_at_pos(self, mat, i, j):
        if self.sum_table[i][j] != -1:
            return self.sum_table[i][j]

    def path_in_matrix(self, mat):
        for row in mat:
            for elem in row:
                print(elem, end=",")
            print()
        return "hello"

def main(f):
    test_case_num = int(f.readline().strip())
    for _ in range(test_case_num):
        mat_dim = int(f.readline().strip())
        pim = PathInMatrix(mat_dim)
        elem_num = 1

        mat = []
        row = []
        for elem in f.readline().strip().split():
            row.append(elem)
            if elem_num % mat_dim == 0:
                mat.append(row)
                row = []
            elem_num += 1

        # print(s1, s2, lcs(s1, s2))
        print(pim.path_in_matrix(mat))

if __name__ == "__main__":
    # import fileinput
    # f = fileinput.input()
    # main(f)

    input_file = "./input.txt"
    with open(input_file, 'r') as f:
        main(f)
