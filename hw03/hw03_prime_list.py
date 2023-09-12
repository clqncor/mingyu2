from mingyu_2.lec01.hw02.lec04_prime_list import is_prime

def main():


    list_prime = [x for x in range(1, 101) if is_prime(x)]
    print(list_prime)


if __name__ == '__main__':
    main()