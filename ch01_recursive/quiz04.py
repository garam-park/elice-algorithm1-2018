'''
최대공약수 구하기
https://academy.elice.io/courses/339/lectures/2416/materials/9
'''
def GCD(x, y) :
    '''
    x, y의 최대공약수를 반환하는 함수
    gcd(x, y) = gcd(y, x%y)
    '''
    tmp = x%y
    if tmp == 0 :
        return y
    return GCD(y, tmp)

def main():
    '''
    Do not change this code
    '''

    data = input()

    x = int(data.split()[0])
    y = int(data.split()[1])

    print(GCD(x, y))

if __name__ == "__main__":
    main()

