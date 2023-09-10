def is_prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count == 2

def main():
    list_prime = [x for x in range(1, 101) if is_prime(x)]
    print(f"1-100까지 중 소수는 {list_prime}입니다.")
    print(f"1-100까지 중 소수의 갯수는 {len(list_prime)}입니다.")

if __name__ == "__main__":
    main()
