class CoinChange(object):
    def __init__(self):
        # TODO: has duplication, when change orders are different
        self.change_methods_of = dict()
        pass

    def change_methods(self, coins, big_money):
        # big_money = change + changed_money
        # change_methods(big_money) = 1 + change_methods(changed_money)

        # get method candidates
        if big_money in self.change_methods_of:
            return self.change_methods_of[big_money]
        small_money_candidates = []
        for change in coins:
            changed = big_money - change
            if changed >= 0:  # legal change method
                small_money_candidates.append(changed)

        if big_money == 0:
            return 1
        elif len(small_money_candidates) == 0:
            return 0

        else:
            num_change_methods = sum(
                [self.change_methods(coins, small_money) for small_money in small_money_candidates]
            )
            self.change_methods_of[big_money] = num_change_methods
            return num_change_methods
        pass


def main(file_handle):
    test_case_num = int(file_handle.readline().strip())
    for _ in range(test_case_num):
        arr_size = int(file_handle.readline().strip())
        sol_instance = CoinChange()

        coins = [int(coin) for coin in file_handle.readline().strip().split()]
        big_money = int(file_handle.readline().strip())

        # print(s1, s2, lcs(s1, s2))
        # pim.print(mat)
        print(sol_instance.change_methods(coins, big_money))
        # pim.print_intermediate()


if __name__ == "__main__":
    # import fileinput
    # f = fileinput.input()
    # main(f)

    input_file = "./input.txt"
    with open(input_file, 'r') as f:
        main(f)
