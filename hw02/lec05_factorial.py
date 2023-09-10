def fac(num):
    result = 1
    for i in range(1, num + 1):
        result *= i

    return result

def main():
    num = int(input('(음수가 아닌 정수를 입력하세요.) \n팩토리얼로 계산할 값을 입력하세요! : '))

    if num > 0:
        print(f'{num}!은 값은' + f'{fac(num)}' + '입니다.')
    else:
        print('음수가 아닌 정수를 입력하세요!!!')


if __name__=="__main__":
    main()