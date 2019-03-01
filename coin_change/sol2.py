MAX_COIN_SIZE = 399


class CoinChange(object):
    def __init__(self, coins):
        self.tableau = dict()
        self.coins = coins
        pass

    def save_and_return(self, function_iter, max_coin_index, big_money):
        if max_coin_index not in self.tableau:
            self.tableau[max_coin_index] = dict()
        methods_count = function_iter(max_coin_index, big_money)
        self.tableau[max_coin_index][big_money] = methods_count
        return methods_count

    def change_methods(self, max_coin_index, big_money):
        # check in tableau
        if max_coin_index in self.tableau:
            if big_money in self.tableau[max_coin_index]:
                return self.tableau[max_coin_index][big_money]

        # check boundary met
        if big_money == 0:
            return 1

        count = 0
        if not max_coin_index - 1 < 0:
            count += self.save_and_return(self.change_methods, max_coin_index - 1, big_money)

        if not big_money - self.coins[max_coin_index] < 0:
            count += self.save_and_return(self.change_methods, max_coin_index,
                                          big_money - self.coins[max_coin_index])

        return count


def main(file_handle):
    test_case_num = int(file_handle.readline().strip())
    for _ in range(test_case_num):
        arr_size = int(file_handle.readline().strip())
        coins = [int(coin) for coin in file_handle.readline().strip().split()]

        sol_instance = CoinChange(coins)
        big_money = int(file_handle.readline().strip())

        print(sol_instance.change_methods(
            max_coin_index=len(coins) - 1,
            big_money=big_money))


if __name__ == "__main__":
    import fileinput
    f = fileinput.input()
    main(f)

    # input_file = "./input.txt"
    # with open(input_file, 'r') as f:
    #     main(f)
