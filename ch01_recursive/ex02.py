'''
quick sort
https://academy.elice.io/courses/339/lectures/2416/materials/4
'''

def quickSort(array):
    
    if len(array)<=1 :
        return array

    pivot = array[0]
    
    left = [x for x in array[1:] if pivot > x]
    right = [x for x in array[1:] if pivot <= x]

    return quickSort(left) + [pivot] + quickSort(right)

def main():
    line = [int(x) for x in input().split()]

    print(*quickSort(line))

if __name__ == "__main__":
    main()
