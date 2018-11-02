'''
k번째 숫자 찾기
https://academy.elice.io/courses/339/lectures/2416/materials/3
'''

def findKth(myInput, k) :
    '''
    매 순간마다 k번째로 작은 원소를 리스트로 반환합니다.
    '''
    result = []

    length = len(myInput)
    
    if length < k:
        return [-1]*(k-1)
    else :
        tmp = findKth(myInput[0:length-1],k)
        result = tmp
        myInput.sort()
        result.append(myInput[k-1])

    return result

def main():
    '''
    테스트를 하고싶으면, 아래 부분을 수정합니다.
    '''

    firstLine = [int(x) for x in input().split()]
    myInput = [int(x) for x in input().split()]

    print(*findKth(myInput, firstLine[1]))
if __name__ == "__main__":
    main()
