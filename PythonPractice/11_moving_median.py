"""
Have the function MovingMedian(arr) read the array of numbers stored in arr which will contain
a sliding window size, N, as the first element in the array and the rest will be a list of numbers. Your
program should return the Moving Median for each element based on the element and its N-1
predecessors, where N is the sliding window size. The final output should be a string with the
moving median corresponding to each entry in the original array separated by commas.

Note that for the first few elements (until the window size is reached), the median is computed on a
smaller number of entries.
For example: if arr is [3, 1, 3, 5, 10, 6, 4, 3, 1] then your program should
output "1,2,3,5,6,6,4,3"

BUGS
"""


def median(arr):
    if len(arr) == 1:
        return arr[0]

    n = len(arr)
    arr = sorted(arr)

    if n % 2 != 0:
        return sorted(arr)[n // 2]
    return (arr[(n // 2) - 1] + arr[(n // 2)]) / 2


def MovingMedian(arr):
    windows = []
    N = arr[0]
    rest = []

    for c in arr[1:]:
        windows.append(c)

    if len(windows) > N:
        windows = windows[1:]
    rest.append(str(median(windows)))
    # Bug or 'res' instead of 'rest - res.append(str(median(windows)))
    return ",".join(rest)


print(MovingMedian([3, 1, 3, 5, 10, 6, 4, 3, 1]))

print("\n\t\t ============== Test Cases ==============")

print("\n--------------------Test case 1-----------------------")
result = MovingMedian([3, 1, 3, 5, 10, 6, 4, 3, 1])
print('Input : [3, 1, 3, 5, 10, 6, 4, 3, 1]')
print("Expected result: 1,2,3,5,6,6,4,3")
print("Actual result   {}".format(result))
result = 0

print("\n--------------------Test case 2-----------------------")
result = MovingMedian([5, 2, 4, 6])
print('Input :[5, 2, 4, 6]')
print("Expected result: 2,3,4")
print("Actual result   {}".format((result)))