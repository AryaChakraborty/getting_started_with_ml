i = map(lambda x : x**3, range(10))
print(list(i))

i = zip(range(10), range(10, 20), range(20, 30))
print(list(i))

l = [1, 2, 3, 4, 5, 10, 23, 12, 90]
result = filter(lambda x : x%2 == 0, l)
print(list(result))

import functools
lis = [1, 2, 3, 4, 5]
curr_ans = functools.reduce(lambda a, b: a+b, lis)
print(curr_ans)