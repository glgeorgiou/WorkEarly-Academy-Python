"""
Have the function MaxSubarray(arr) take the array of numbers stored in arr and determine the
largest sum that can be formed by any contiguous subarray in the array.
For example, if arr is [-2, 5, -1, 7, -3] then your program should return 11
because the sum is formed by the subarray [5, -1, 7].
Adding any element before or after this subarray would make the sum smaller.
"""


def MaxSubarray(arr):

  # code goes here
  max_sum = 0
  for i in range(len(arr)):
    j = i
    temp_sum = 0
    while (j<len(arr)):
      temp_sum += arr[j]
      if (temp_sum < 0 and max_sum == 0):
        max_sum = temp_sum
      elif max_sum < temp_sum:
        max_sum = temp_sum
      j += 1
  return max_sum


print("\n\t\t ============== Test Cases ==============")

print("\n--------------------Test case A-----------------------")
result = MaxSubarray([1, -2, 0, 3])
print('Input : [1, -2, 0, 3]')
print("Expected result: 3")
print("Actual result   {}".format(result))
result = 0

print("\n--------------------Test case B-----------------------")
result = MaxSubarray([3, -1, -1, 4, 3, -1])
print('Input : [3, -1, -1, 4, 3, -1]')
print("Expected result: 8")
print("Actual result   {}".format(result))