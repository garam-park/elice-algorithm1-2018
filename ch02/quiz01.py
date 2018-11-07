def diffDigit(_a, _b) :
    '''
    a, b의 서로 다른 자리수의 개수를 반환한다
    '''
    a = str(_a)
    b = str(_b)

    _max = max(len(a),len(b))
    _min = min(len(a),len(b))

    ret = _max -_min
    
    a = a[::-1]
    b = b[::-1]

    for i in range(_min):
        if a[i] != b[i] :
            ret = ret + 1

    return ret

def main():
    '''
    Do not change this code
    '''

    # a = int(input())
    # b = int(input())
    a = 1234
    b = 12345123

    print(diffDigit(a, b))


if __name__ == "__main__":
    main()
