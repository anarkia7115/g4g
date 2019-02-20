class EditDistance(object):
    def __init__(self):

        self.dis_table = dict()

    @staticmethod
    def emphasis_i(s1, i):
        if i+1 < len(s1):
            return s1[:i]+'['+s1[i]+']'+s1[i+1:]
        else:
            return s1 + "[]"




    def edit_dis(self, s1, s2):
        # print("comparing: ", emphasis_i(s1, i), emphasis_i(s2, i))
        # final condition
        if s1 == s2:
            return 0

        # read from mem
        if s1 in self.dis_table and s2 in self.dis_table[s1]:
            return self.dis_table[s1][s2]
        else:
            #print("{} not in {} or [{}] not in {}".format(s1, self.dis_table.keys(), s2, self.dis_table))
            pass

        # check bound
        if len(s1) == 0 and len(s2) > 0:
            # delete longer
            dis_return = len(s2)
            # print("dist between [{}] and [{}] is {}:".format(s1, s2, dis_return))
            if s1 not in self.dis_table:
                self.dis_table[s1] = dict()
            self.dis_table[s1][s2] = dis_return
            return dis_return
        if len(s2) == 0 and len(s1) > 0:
            dis_return = len(s1)
            # print("dist between [{}] and [{}] is {}:".format(s1, s2, dis_return))
            if s1 not in self.dis_table:
                self.dis_table[s1] = dict()
            self.dis_table[s1][s2] = dis_return
            return dis_return

        # all 4 distance
        # if same char, pass
        if s1[0] == s2[0]:  # no move
            dis_return = self.edit_dis(s1[1:], s2[1:])
            # print("dist between {} and {} is {}:".format(s1, s2, dis_return))
            if s1 not in self.dis_table:
                self.dis_table[s1] = dict()
            self.dis_table[s1][s2] = dis_return
            return dis_return
        else:  # 3 moves
            # s1 insert <=> s2 delete
            # insert
            # print("insert")
            dis_i = self.edit_dis(s1, s2[1:]) + 1
            # delete
            # print("delete")
            dis_d = self.edit_dis(s1[1:], s2) + 1
            # replace
            # print("replace")
            dis_r = self.edit_dis(s1[1:], s2[1:]) + 1

            # compare distance
            dis_return = 0
            if dis_i <= dis_d and dis_i <= dis_r:
                dis_return = dis_i
            elif dis_d <= dis_i and dis_d <= dis_r:
                dis_return = dis_d
            elif dis_r <= dis_i and dis_r <= dis_d:
                dis_return = dis_r

            # print("dist between {} and {} is {}:".format(s1, s2, dis_return))
            if s1 not in self.dis_table:
                self.dis_table[s1] = dict()
            self.dis_table[s1][s2] = dis_return
            return dis_return


def main(f):
    test_case_num = int(f.readline().strip())
    for _ in range(test_case_num):
        f.readline() # skip one line
        s1, s2 = f.readline().strip().split()
        ed = EditDistance()
        # print(s1, s2, lcs(s1, s2))
        print(ed.edit_dis(s1, s2))


if __name__ == "__main__":
    # import fileinput
    # f = fileinput.input()
    # main(f)

    input_file = "./input.txt"
    with open(input_file, 'r') as f:
        main(f)
