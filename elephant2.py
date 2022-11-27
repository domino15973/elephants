#solution to task 'elephants' version 2

def main():
    n = int(input())
    m = list(map(int, input().split(' ')))
    a = list(map(lambda x: int(x), input().split(' ')))
    b = list(map(lambda x: int(x), input().split(' ')))

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

    print(w)


if __name__ == '__main__':
    main()
