"""
You have an empty sequence, and you will be given

queries. Each query is one of these three types:

1 x  -Push the element x into the stack.
2    -Delete the element present at the top of the stack.
3    -Print the maximum element in the stack.

"""

stack = [0]
n = int(input())
for i in range(n):
    nums = list(map(int, input().split()))
    if nums[0] == 1:
        stack.append(max(nums[1], stack[-1]))
    elif nums[0] == 2:
        stack.pop()
    else:
        print(stack[-1])