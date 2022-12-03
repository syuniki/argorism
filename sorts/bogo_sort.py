import random
from typing import List


def in_order(numbers: List[int]) -> bool:
    # Pythonのリスト内包括という書き方らしい (式 for i in ...)
    return all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1))
    # for i in range(len(numbers)-1):
    #     if numbers[i] > numbers[i+1]:
    #         return False
    # return True


def bogo_sort(numbers: List[int]) -> List[int]:
    count = 0
    while not in_order(numbers):
        count += 1
        random.shuffle(numbers)
    print(count)
    return numbers


if __name__ == '__main__':
    nums = [random.randint(0, 1000) for _ in range(5)]
    print(nums)
    print(bogo_sort(nums))

# [495, 856, 983, 654, 996] 並び替え前
# 138 試行回数
# [495, 654, 856, 983, 996] 並び替え後
