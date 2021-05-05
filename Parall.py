from multiprocessing import Process, Pool
import csv
from math import ceil
from itertools import repeat

def element(index, A, B):
    i, j = index
    res = 0
    # get a middle dimension
    N = len(A[0])
    for k in range(N):
        res += A[i][k] * B[k][j]
    print(res)
    with open("out.csv", "r+", newline="") as f:
        matrx_tmp = list(csv.reader(f))
        matrx_tmp[i][j] = res
        f.seek(0)
        csv.writer(f).writerows(matrx_tmp)
        # f.truncate()


def multi_run_wrapper(args):
    print(*args)
    return element(*args)


if __name__ == '__main__':
    with open('matrix1.csv', 'r') as f:
        A = [[int(num) for num in line.split(';')] for line in f]
    with open('matrix2.csv', 'r') as f:
        B = [[int(num) for num in line.split(';')] for line in f]
    with open("out.csv", "w", newline="") as f:
        C = [[0 for _ in range(len(B[0]))] for __ in range(len(A))]
        csv.writer(f).writerows(C)
    procs = []
    #допустим количество необходимых параллельных потоков рассчитывается как количество элементов исходной матрицы/5, тогда:
    pool_val = ceil(len(C[0])*len(C)/5)
    index_list = []
    for i in range(len(A)):
        for j in range(len(B[0])):
            index_list.append((i, j))
    pool = Pool(pool_val)
    index_list = [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
    pool.starmap(element, zip(index_list, repeat(A), repeat(B)))