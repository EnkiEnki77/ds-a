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





