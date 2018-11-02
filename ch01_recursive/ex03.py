'''
올바른 괄호인지 판단하기
https://academy.elice.io/courses/339/lectures/2416/materials/5
'''

def checkParen(p):

    if len(p) == 0:
        return "YES"

    if len(p) == 2:
        if p == "()":
            return "YES"
        else:
            return "NO"
    
    for i in range(0,len(p)-1):
        if p[i] == "(" and p[i+1] == ')'
            tmp = p[:i] + p[i+2:]
            return checkParen(tmp)
    
    return "NO"

def main():
    '''
    Do not change this code
    '''

    x = input()
    print(checkParen(x))

if __name__ == "__main__":
    main()


