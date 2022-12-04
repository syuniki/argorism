from typing import List


def insertion_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(1, len_numbers):
        temp = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > temp:
            # 値が大きかった時に、先に項番を一つ後ろにずらしておく
            numbers[j+1] = numbers[j]
            j -= 1
        # tempに持っていた値を、挿入
        numbers[j+1] = temp

    return numbers


if __name__ == "__main__":
    import random
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(insertion_sort(nums))
