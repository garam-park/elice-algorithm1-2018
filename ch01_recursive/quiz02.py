'''
문자열 포함 관계 조사

https://academy.elice.io/courses/339/lectures/2416/materials/7

mef
myself

=> Yes

abca
acf

=> No
'''

import sys
sys.setrecursionlimit(100000)

def strContain(A, B) :
    '''
    문자열 A의 알파벳이 문자열 B에 모두 포함되어 있으면 "Yes", 아니면 "No"를 반환합니다.
    '''
    
    if len(A) > 0 :
        if A[0] in B:
            return strContain(A[1:],B)
        else :
            return "No"
    
    return "Yes"

def main():
    '''
    Do not change this code
    '''

    A = input()
    B = input()

    print(strContain(A, B))

if __name__ == "__main__":
    main()
