def fib(number):
    a, b = 0, 1
    while number:
        number -= 1
        a, b = b, a + b
    return a    

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()