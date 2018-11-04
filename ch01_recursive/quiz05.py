'''
순열 구하기
https://academy.elice.io/courses/339/lectures/2416/materials/10
'''

c = ['a','b','c','d','e','f','g','h','i','j']

def getPermutation(n, r) :
    '''
    n개의 알파벳 중에서 r개를 뽑아 나열한 결과를 리스트로 반환합니다.

    예를 들어, n = 4, r = 2 일 경우에는
    
    ["ab", "ac", "ad", "ba", "bc", "bd", "ca", "cb", "cd", "da", "db", dc"] 를 반환합니다.
    '''
    result = []
    
    if r == 0 :
        return []

    for i in range(0,n):
        
        tmps = getPermutation(n,r-1)
        
        if len(tmps) > 0 :
            p_ret = [ c[i] + x for x in tmps if c[i] not in x]
        else :
            p_ret = [c[i]]

        result.extend(p_ret)

    return result

def main():
    '''
    테스트를 하고싶으면, 아래 부분을 수정합니다.
    '''

    # firstLine = [int(x) for x in input().split()]
    firstLine = [4,2]

    print('\n'.join(getPermutation(firstLine[0], firstLine[1])))

if __name__ == "__main__":
    main()
