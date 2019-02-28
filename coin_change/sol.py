MAX_COIN_SIZE = 399


class CoinChange(object):
    def __init__(self):
        # self.change_methods_of = dict()
        pass

    def change_methods(self, coins, big_money, last_coin_size):
        # big_money = change + changed_money
        # change_methods(big_money) = 1 + change_methods(changed_money)

        # get method candidates
        # if big_money in self.change_methods_of:
        #     return self.change_methods_of[big_money]
        change_coin_candidates = []
        for coin in coins:
            if coin > last_coin_size:
                continue
            small_money = big_money - coin
            if small_money >= 0:  # legal change method
                change_coin_candidates.append(coin)

        if big_money == 0:
            return 1
        elif len(change_coin_candidates) == 0:
            return 0

        else:
            # sum
            num_change_methods = sum(
                [self.change_methods(coins, big_money - change_coin, change_coin) for change_coin in change_coin_candidates]
            )
            # self.change_methods_of[big_money] = num_change_methods
            return num_change_methods
        pass


def main(file_handle):
    test_case_num = int(file_handle.readline().strip())
    for _ in range(test_case_num):
        arr_size = int(file_handle.readline().strip())
        sol_instance = CoinChange()

        coins = [int(coin) for coin in file_handle.readline().strip().split()]
        big_money = int(file_handle.readline().strip())

        print(sol_instance.change_methods(coins, big_money, MAX_COIN_SIZE))


if __name__ == "__main__":
    # import fileinput
    # f = fileinput.input()
    # main(f)

    input_file = "./input.txt"
    with open(input_file, 'r') as f:
        main(f)
