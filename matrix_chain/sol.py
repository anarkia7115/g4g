class MatrixChainMultiplication(object):
    def __init__(self):
        self.tableau = dict()
        pass

    def save_and_return(self, compute_operation, max_coin_index, big_money):
        if max_coin_index not in self.tableau:
            self.tableau[max_coin_index] = dict()
        methods_count = compute_operation(max_coin_index, big_money)
        self.tableau[max_coin_index][big_money] = methods_count
        return methods_count

    def compute_min_operations(self, matrix_dims):
        pass

def main(file_handle):
    test_case_num = int(file_handle.readline().strip())
    for _ in range(test_case_num):
        arr_size = int(file_handle.readline().strip())
        coins = [int(coin) for coin in file_handle.readline().strip().split()]

        sol_instance = MatrixChainMultiplication()
        big_money = int(file_handle.readline().strip())

        print(sol_instance.compute_min_operations(matrix_dims))


if __name__ == "__main__":
    import fileinput
    f = fileinput.input()
    main(f)

    # input_file = "./input.txt"
    # with open(input_file, 'r') as f:
    #     main(f)
