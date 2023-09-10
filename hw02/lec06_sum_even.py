
def main():
    print(f'1-100까지 짝수의 합은 {sum([x for x in range(1,101) if x % 2==0])}입니다.')

if __name__=="__main__":
    main()