def is_prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count == 2

def main():
    first, last = map(int,input(f" 빈칸에 원하는 수를 입력하세요 => []부터 []까지 중 소수를 구하자! ").split(' '))
    list_prime = [x for x in range(first, last+1) if is_prime(x)]
    print(f"1-100까지 중 소수는 {(list_prime)}입니다.")
    print(f"1-100까지 중 소수의 갯수는 {len(list_prime)}입니다.")


if __name__ == "__main__":
    main()
