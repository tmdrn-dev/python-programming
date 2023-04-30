# https://heytech.tistory.com/79

from bisect import bisect_left, bisect_right

arr = [5, 6, 7, 7, 7, 7, 8, 8, 9, 10]

# 값이 9인 원소 개수 출력
lindex = bisect_left(arr, 9)
rindex = bisect_right(arr, 9)
print(rindex-lindex)

# [4, 7] 범위 내에 있는 원소 개수 출력
lindex = bisect_left(arr, 4)
rindex = bisect_right(arr, 7)
print(arr[lindex:rindex])