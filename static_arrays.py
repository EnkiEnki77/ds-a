# When an array is initialized it is allocated contiguous space in memory for each value. Each of these
# spaces in memory has an associated address with an index mapped to it. Arrays are fixed size, meaning
# Additional indexes cannot be allocated after initialization. This is because we would have no control
# over whether the additional memory space allocated is contiguous with the rest of the array, and if it
# isn't it would not be considered a part of the original array
myArray = [1,2,3,4,5]



# You can then access an arbitrary element, replacing i with the index of whatever element you're trying
# to access. Regardless of the size of the array the time it takes to access a single index is always
# constant, making the time complexity O(1). It is instant because each index is directly mapped to an
# address in RAM.
# myArray[i]

# A worst case scenario of O(1) is most efficient, but does not mean it's always fast. There could still
# be 1000 operations if that's how big the array is. It just means that the number of operations does not
# grow as the size of the data or input grows. It stays the same no matter how big the array is. Even if
# array has 1000 elements accessing 1 element is only 1 operation. Since we have direct access to its
# address in memory.



# We can read all values in an array by traversing through it with a loop. The time complexity of traversing
# an array is O(n) because the number of operations grows linearly with the size of the array. If there are
# 5 elements in the array there will be 5 operations, if there are 1000 elements, then 1000 operations.
for i in range(len(myArray)):
    print(myArray[i])

# OR

i = 0
while i < len(myArray):
    print(myArray[i])
    i += 1



# When an array indice is empty it will have a placeholder value in memory denoting it's empty. The allocated
# space for that index is never deleted though, even if you remove an element from the array.

# If we remove the last element from the array the valuue in memory is replaced by a placeholder such as null
# 0, or -1 to indicate it's empty. This is called a soft delete. If the allocated memory was removed along
# with the element the array would then be permanently smaller. You could no longer add another value back
# into the array. The memory for the array must always stay fixed. The length of the array is also reduced by
# 1.

def remove_end(arr, length):
    # If array isn't empty
    if length > 0:
        # Replace last element in array with a value denoting it's empty.
        arr[length - 1] = 0

remove_end(myArray, len(myArray))



# Deleting the element at the very end of the array would be a time complexity of O(1), because we have
# direct access to the element through it's index, and deleting it does not make the arrays remaining value
# non-contiguous.
# However, if we were to delete a value in the middle of the array, this would make the array non-contiguous
# This means we need to actually shift all the elements in front of the one we're deleting to the left one
# space, and denote that the last space in the array is empty with null or -1

def remove_middle(arr, i, length):
#     Start shifting the elements starting from the element in front of the one we're removing
    for index in range(i + 1, length):
        # Moving the element at index one space to the left in the array. This will overwrite the element
        # we're trying to remove, and leave one empty index at the end of the array.
        arr[index - 1] = arr[index]

remove_middle(myArray, 1, len(myArray))

# The worst case would be we have to shift every element in the array, where the target of removal is
# the first index. This makes the time complexity O(n)



# If we want to insert an element at the end of the array we would simply overwrite the value denoting the
# index is empty with our value. Assuming it's empty. This is an O(1) operation.

# Insert n into arr at the next open position.
# Length is the number of 'real' values in arr, and capacity
# is the size (aka memory allocated for the fixed size array).
def insertEnd(arr, n, length, capacity):
    if length < capacity:
        arr[length] = n



# To insert an element in the middle of the array, assuming there is free space, we need to first shift
# the elements at the index currently along with all the elements after it to the right so that they are
# not overwritten. We can then insert the new value afterward, and increase the length by 1.
# If the array is full when you insert into it the last value in the array will be lost.
# Time complexity is O(n)

# Insert n into index i after shifting elements to the right.
# Assuming i is a valid index and arr is not full.
# Length is the amount of non-empty values in the array.
def insertMiddle(arr, i, n, length):
    # Shift starting from the end to i.
    for index in range(length - 1, i - 1, -1):
        arr[index + 1] = arr[index]

    # Insert at i
    arr[i] = n



