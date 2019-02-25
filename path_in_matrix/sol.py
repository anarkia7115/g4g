class PathInMatrix(object):
    def __init__(self, mat_dim):
        self.sum_table = [[-1 for _ in range(mat_dim)] for _ in range(mat_dim)]

    def assign_sum_table_and_return(self, tbl_i, tbl_j, opt_sum):
        self.sum_table[tbl_i][tbl_j] = opt_sum
        # self.print_intermediate()
        # print()
        return opt_sum

    def max_sum_at_pos(self, mat, i_row, j_col):
        if self.sum_table[i_row][j_col] != -1:
            return self.sum_table[i_row][j_col]
        # else
        # only two options, left or right
        # check row index is able to go up
        # left
        if i_row - 1 < 0:
            # optimal sum is itself
            return self.assign_sum_table_and_return(i_row, j_col, mat[i_row][j_col])
        sum_candidates = []
        if j_col - 1 >= 0:
            sum_candidates.append(self.max_sum_at_pos(mat, i_row-1, j_col-1))
        if j_col + 1 < len(mat):
            sum_candidates.append(self.max_sum_at_pos(mat, i_row-1, j_col+1))
        if len(sum_candidates) == 0:  # almost not possible
            # optimal sum is itself
            return self.assign_sum_table_and_return(i_row, j_col, mat[i_row][j_col])
        return self.assign_sum_table_and_return(i_row, j_col,  mat[i_row][j_col] + max(sum_candidates))

    @staticmethod
    def print(mat):
        for row in mat:
            for elem in row:
                print(elem, end=", ")
            print()

    def print_intermediate(self):
        self.print(self.sum_table)

    def path_in_matrix(self, mat):
        init_i_row = len(mat) - 1
        optimal_candidates = []
        for init_j_col in range(len(mat)):
            optimal_candidates.append(self.max_sum_at_pos(mat, init_i_row, init_j_col))
        return max(optimal_candidates)


def main(f):
    test_case_num = int(f.readline().strip())
    for _ in range(test_case_num):
        mat_dim = int(f.readline().strip())
        pim = PathInMatrix(mat_dim)
        elem_num = 1

        mat = []
        row = []
        for elem in f.readline().strip().split():
            row.append(int(elem))
            if elem_num % mat_dim == 0:
                mat.append(row)
                row = []
            elem_num += 1

        # print(s1, s2, lcs(s1, s2))
        # pim.print(mat)
        print(pim.path_in_matrix(mat))
        # print(pim.print_intermediate())

if __name__ == "__main__":
    # import fileinput
    # f = fileinput.input()
    # main(f)

    input_file = "./input.txt"
    with open(input_file, 'r') as f:
        main(f)
