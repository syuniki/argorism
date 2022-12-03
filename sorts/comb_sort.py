from typing import List


def comb_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    gap = len_numbers
    swapped = True

    while gap != 1 or swapped:
        # 配列の長さを 1.3 で割ったものがチェックする間隔
        gap = int(gap / 1.3)
        if gap < 1:
            # 間隔が1になるまで繰り返す
            gap = 1

        swapped = False

        for i in range(0, len_numbers - gap):
            if numbers[i] > numbers[i + gap]:
                numbers[i], numbers[i + gap] = numbers[i + gap], numbers[i]
                # 入れ替えが発生している
                swapped = True

    return numbers


if __name__ == "__main__":
    import random
    nums = [random.randint(0, 1000) for i in range(10)]
    print(comb_sort(nums))
