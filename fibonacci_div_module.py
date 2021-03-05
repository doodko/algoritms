def fib_mod(n, m):
    lst = [0]
    a, b = 0, 1
    while True:
        a, b = b, a + b
        lst.append(a % m)
        if lst[-1] == 1 and lst[-2] == 0 and len(lst) > 2:
            period = len(lst) -2
            break

    return lst[n % period]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()