import sys

def powerSet(arr) : 
    
    if len(arr) == 1:
        return [[],arr]
    else :
        result = []
        subs = powerSet(arr[1:]);
        for sub in subs:
            
            
            #없는 것
            tmp2 = sub
            result.append(sub)           
            
            #있는 것
            tmp1 = sub.copy();
            result.append([arr[0]] + tmp1)
    result.sort()
    
    return result

def makeEqual(data) :
    '''
    n개의 숫자를 두 그룹 A, B로 나눈다고 할 때,

    | (A의 원소의 합) - (B의 원소의 합) | 의 최솟값을 반환하는 함수를 작성하시오.
    '''

    s = sum(data)
    ps = powerSet(data)

    ret = 9999999
    for p in ps:
        a = sum(p)
        ret = min(abs(2*a - s),ret)

    return ret

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]

    print(makeEqual(data))

if __name__ == "__main__":
    main()
