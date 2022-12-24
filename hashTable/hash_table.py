from typing import Any
import hashlib


class HashTable:

    def __init__(self, size=10) -> None:
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash(self, key) -> int:
        # keyをハッシュ値に変換して、intに変換
        return int(hashlib.md5(key.encode()).hexdigest(), base=16) % self.size

    def add(self, key, value) -> None:
        index = self.hash(key)
        for data in self.table[index]:
            # 同じkeyが存在していた場合
            if data[0] == key:
                data[1] = value
                break
        else:
            self.table[index].append([key, value])

    def get(self, key) -> Any:
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                return data[1]

    def print(self) -> None:
        for index in range(self.size):
            print(index, end=" ")
            for data in self.table[index]:
                print("-->", end=" ")
                print(data, end=" ")
            print()

    # インスタンス[key] = value の形式で値のセットができる
    def __setitem__(self, key, value) -> None:
        self.add(key, value)

    # インスタンス[key] の形式で値のゲットができる
    def __getitem__(self, key) -> Any:
        return self.get(key)


if __name__ == '__main__':
    hash_table = HashTable()
    # hash_table.add("car", "Tesla")
    # hash_table.add("car", "Toyota")
    # hash_table.add("pc", "Mac")
    # hash_table.add("sns", "YouTube")
    # hash_table.add("language", "Python")
    # hash_table.print()
    # print(hash_table.get("car"))
    # print(hash_table.get("sns"))
    # print(hash_table.get(""))
    hash_table["car"] = 'Tesla'
    hash_table["pc"] = 'Mac'
    hash_table.print()
    print(hash_table["car"])
