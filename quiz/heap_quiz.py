'''
出現するワードの回数によるランキング(トップN)をheapを用いて導く
'''
import collections
import heapq
from typing import List


def top_n_with_heap(words: List[str], n: int) -> List[str]:
    # d = {}
    # for word in words:
    #     # keyが存在しない場合はデフォルトで0が入る
    #     d[word] = d.get(word, 0) + 1
    # print(d)
    counter_word = collections.Counter(words)
    # heapqだと最小の数が取れるので、一番出現回数が多いものが最小になるように 、出現回数を-に反転させる。
    data = [(-counter_word[word], word) for word in counter_word]
    size = n if len(data) > n else len(data)
    heapq.heapify(data)
    return [heapq.heappop(data)[1] for _ in range(size)]


if __name__ == "__main__":
    words = ["python", 'c', "java", 'go', "python", "c", "go", "python"]
    print(top_n_with_heap(words, 2))
