import sys
from glob import glob


def data_loading(filepath):
    file = open(filepath, "r")
    elephant = file.read()
    elephant = elephant.split('\n')
    elephant = [l.split(' ') for l in elephant]
    elephant.pop()
    file.close()

    n = int(elephant[0][0])             # number of elephants
    m = list(map(int, elephant[1]))     # mass
    a = list(map(int, elephant[2]))     # start
    b = list(map(int, elephant[3]))     # destination

    return n, m, a, b


def main(n, m, a, b):
    p = [0 for _ in range(n)]

    for i in range(n):
        p[b[i] - 1] = a[i] - 1

    odw = [False for _ in range(n)]
    C = []
    for i in range(n):
        if not odw[i]:
            c = [i]
            odw[i] = True
            x = p[i]
            while odw[x] is not True:
                odw[x] = True
                c.append(x)
                x = p[x]
            C.append(c)

    mass_sum = [sum([m[s] for s in c]) for c in C]
    min_c = [min([m[s] for s in c]) for c in C]
    min_all = min(m)

    w = 0
    for ci, c in enumerate(C):
        method1 = mass_sum[ci] + (len(c) - 2) * min_c[ci]
        method2 = mass_sum[ci] + min_c[ci] + (len(c) + 1) * min_all
        w += min(method1, method2)

    return w


def check(filepath):
    file = open(filepath, "r")
    output = file.read()
    output = output.split('\n')
    output.pop()
    file.close()

    result = int(output[0])

    return result


if __name__ == '__main__':
    filename_in = [glob('slo*.in')]
    filename_out = [glob('slo*.out')]
    for i in range(len(filename_in[0])):
        n, m, a, b = data_loading(filename_in[0][i])
        w = main(n, m, a, b)
        result = check(filename_out[0][i])
        if result == w:
            print(filename_in[0][i], '=', w)
        else:
            sys.exit('error')
