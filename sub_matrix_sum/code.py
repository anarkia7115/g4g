from typing import List


def accumulate_matrix(mat):
    row_size = len(mat[0])
    amat = []
    arow = [0] * row_size
    for row in mat:
        row_sum = 0
        for i in range(len(row)):
            elem = row[i]
            row_sum += elem
            arow[i] += row_sum
        amat.append(arow[:])
    return amat

def optimized_compute_sum(mat:List[List[int]], tli, tlj, rbi, rbj):
    # accumulate matrix
    amat = accumulate_matrix(mat)

    rst = 0
    rst =  amat[rbi][rbj]
    if tli-1 >= 0:
        rst -= amat[tli-1][rbj]
    if tlj-1 >= 0:
        rst -= amat[rbi][tlj-1]
    if tli-1 >= 0 and tlj-1 >=0:
        rst += amat[tli-1][tlj-1]
    return rst


def compute_sum(mat:List[List[int]], tli, tlj, rbi, rbj):
    rst = 0
    for i in range(tli, rbi+1):
        for j in range(tlj, rbj+1):
            rst += mat[i][j]
    return rst


def print_mat(m):
    for row in m:
        for elem in row:
            print("%5d"%elem,end="")
        print()

def main():
    """
tli :  Row number of top left of query submatrix
tlj :  Column number of top left of query submatrix
rbi :  Row number of bottom right of query submatrix
rbj :  Column number of bottom right of query submatrix

Input: mat[M][N] = {{1, 2, 3, 4, 6},
                    {5, 3, 8, 1, 2},
                    {4, 6, 7, 5, 5},
                    {2, 4, 8, 9, 4} };
Query1: tli = 0, tlj = 0, rbi = 1, rbj = 1
Query2: tli = 2, tlj = 2, rbi = 3, rbj = 4
Query3: tli = 1, tlj = 2, rbi = 3, rbj = 3;

Output:
Query1: 11  // Sum between (0, 0) and (1, 1)
Query2: 38  // Sum between (2, 2) and (3, 4)
Query3: 38  // Sum between (1, 2) and (3, 3)
    """
    mat = [
        [1,2,3,4,6],
        [5,3,8,1,2],
        [4,6,7,5,5],
        [2,4,8,9,4]
    ]
    amat = accumulate_matrix(mat)
    print("mat:")
    print_mat(mat)
    print("amat:")
    print_mat(amat)
    print(optimized_compute_sum(mat, 0, 0, 1, 1))
    print(optimized_compute_sum(mat, 2, 2, 3, 4))
    print(optimized_compute_sum(mat, 1, 2, 3, 3))
    # print(compute_sum(mat, 0, 0, 1, 1))
    # print(compute_sum(mat, 2, 2, 3, 4))
    # print(compute_sum(mat, 1, 2, 3, 3))


if __name__ == "__main__":
    main()