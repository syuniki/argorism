'''
1. Input: [11, 2, 5, 9, 10, 3], 12 => Output: (2, 10) or None
2. Input: [11, 2, 5, 9, 10, 3] => Output: (11, 9) or None  ex) 11 + 9 = 2 + 5 + 10 + 3
'''

from typing import List, Tuple, Optional


# 1の回答(複数の組み合わせ取得ver ※組み合わせない時にNoneではなく空配列が返却される)
def get_pair(numbers: List[int], target: int) -> Optional[List[Tuple[int, int]]]:
    cache = set()
    result = []
    for num in numbers:
        val = target - num
        if val in cache:
            result.append((val, num))
        cache.add(num)
    return result


# ２の回答(複数の組み合わせver)
def get_pair_half_sum(numbers: List[int]) -> Optional[List[Tuple[int, int]]]:
    list_sum = sum(numbers)
    half_sum, remainder = divmod(list_sum, 2)
    if remainder == 0:
        half_sum = list_sum // 2
        return get_pair(numbers, half_sum)


if __name__ == '__main__':
    nums = [11, 2, 5, 9, 10, 3]
    print(get_pair(nums, 12))
    print(get_pair_half_sum(nums))
