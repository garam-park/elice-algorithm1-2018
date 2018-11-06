import sys

def getSubsum(data) :
	tmp = -99999999
	for i in range(len(data)):
		for j in range(i,len(data)):
			tmp = max(tmp,sum(data[i:j+1]))
			
	return tmp

def main():
    '''
    이 부분은 수정하지 마세요.
    '''

    data = [int(x) for x in input().split()]

    print(getSubsum(data))

if __name__ == "__main__":
    main()
