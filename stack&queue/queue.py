from collections import deque
from typing import Any


class Queue:
    def __init__(self) -> None:
        self.queue = []

    def enqueue(self, data: Any) -> None:
        self.queue.append(data)

    def dequeue(self) -> Any:
        if self.queue:
            return self.queue.pop(0)


def reverse(queue: deque) -> deque:
    new_queue = deque()
    while queue:
        new_queue.append(queue.pop())
    [queue.append(d) for d in new_queue]
    # return new_queue


if __name__ == "__main__":
    # dequeライブラリの利用
    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    q.append(4)
    print(q)
    reverse(q)
    print(q)

    # 自作クラスの利用
    # q = Queue()
    # q.enqueue(1)
    # q.enqueue(2)
    # q.enqueue(3)
    # q.enqueue(4)
    # print(q.queue)
    # print(q.dequeue())
    # print(q.dequeue())
    # print(q.queue)
    # print(q.dequeue())
    # print(q.dequeue())
