def numDivisor(n):
    '''
    n의 약수의 개수를 반환하는 함수를 작성하세요.
    '''

    #배열 n
    arr = [-1]
    #초기화 O(n)
    for i in range(1,n+1):
        arr.append(0)

    #모든 거 (n)
    for i in range(1,n+1):
        if arr[i] != 0:
            continue
        else :
            if n%i == 0:
                arr[i] = 1
            else :
                arr[i] = -1
    ret = 0
    for i in range(1,n+1):
        if arr[i] == 1:
            ret = ret + 1
    
    return ret

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    number = int(input())
    print(numDivisor(number))

if __name__ == "__main__":
    main()
