import sys

def _powerSet(a,b):

    res = []

    if a == b:
        return [[],[a]]

    subs = _powerSet(a,b-1)

    for sub in subs:
        res.append(sub)
        tmp = sub.copy()
        tmp.append(b)
        res.append(tmp)

    return res

def powerSet(n) :
    '''
    n개의 원소를 가지는 집합 A의 멱집합의 원소를 사전 순서대로 list로 반환하는 함수를 작성하시오.

    예를 들어, n = 3 일 경우 다음의 list를 반환한다.

    [ [1], [1, 2], [1, 3], [1, 2, 3], [2], [2, 3], [3] ]
    '''
    ret = _powerSet(1,n)
    ret.sort()
    ret.remove([])

    return ret

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    n = int(input())

    result = powerSet(n)
    
    for line in result :
        print(*line)

if __name__ == "__main__":
    main()
