def recursive_nth_fibo(idx):
    if idx == 0:
        return 0
    elif idx == 1:
        return 1
    else:
        return recursive_nth_fibo(idx - 1) + recursive_nth_fibo(idx - 2)


def main():
    idx = int(input("Zadej pocet prvku: "))

    fib_seq = [recursive_nth_fibo(num) for num in range(idx + 1)]
    print(fib_seq)


if __name__ == '__main__':
    main()
