'''
문자열 뒤집기
https://academy.elice.io/courses/339/lectures/2416/materials/8
'''
def stringReverse(myString) :
    '''
    문자열 myString을 뒤집어서 반환하는 함수를 작성하세요.
    '''
    if len(myString) <= 1:
        return myString
    return myString[-1]+stringReverse(myString[1:-1])+myString[0]

def main():
    '''
    테스트를 하고싶으면, 아래 부분을 수정합니다.
    '''

    myString = input()

    print(stringReverse(myString))
if __name__ == "__main__":
    main()
