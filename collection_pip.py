import collections

nums = [1,2,4,5]

deque = collections.deque(nums)

print(deque)

deque.append(9)
deque.appendleft(0)
print(deque)