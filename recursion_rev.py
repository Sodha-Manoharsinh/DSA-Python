# num = [1,2,3,4,5,6,7,8,9]
num = [5,7,3,2,6,1,5,9]

def fun(left,right,arr):
    if len(arr) == 0:
        return
    
    if left > right:
        return 

    temp = arr[left]
    arr[left] = arr[right]
    arr[right] = temp

    fun(left+1,right-1,arr)

fun(2,5,num)
print(num)