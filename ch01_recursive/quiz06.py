'''
가로수
https://academy.elice.io/courses/339/lectures/2416/materials/11
'''
def gcd(a, b):
    if b > a:
        if b % a == 0:
            return a
        else:
            return gcd(b % a, a)
    else:
        if a % b == 0:
            return b
        else:
            return gcd(b, a % b)    

def howManyTree(n, myInput) :

	myInput.sort()
			
	gabs = []
			
	for i in range(n-1):
		gab = myInput[i+1] - myInput[i]
		gabs.append(gab)

	gabs.sort()
	v = gabs[-1]
	for i in range(0,len(gabs)-1) :
		tmp = gcd(gabs[i],gabs[i+1])
		if tmp == 1 :
			v = 1
			break
		else:
			if tmp < v :
				v = tmp
			

	dis   = (myInput[-1] - myInput[0])//v + 1
	cnt = dis - n
			
	return int(cnt)

def main():
    '''
    수정하시면 안됩니다.
    '''
    n = int(input())
    myInput = []
    for _ in range(n) :
        myInput.append(int(input()))

    print(howManyTree(n, myInput))
if __name__ == "__main__":
    main()
