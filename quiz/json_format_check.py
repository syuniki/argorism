'''カッコの開閉の数がそろっているかチェックする
Input: {'key1': 'value1', 'key2': [1, 2, 3], 'key3': (1, 2, 3)} => Output: True
Input: {'key1': ['value1', 'key2': [1, 2, 3], 'key3': (1, 2, 3)} => Output: False
'''


def validate_format(chars: str) -> bool:
    lookup = {'{': '}', '[': ']', '(': ')'}
    stack = []

    for char in chars:
        if char in lookup.keys():
            stack.append(lookup[char])
        if char in lookup.values():
            if not stack:
                return False
            if char != stack.pop():
                return False

    if stack:
        return False

    return True


if __name__ == "__main__":
    print(validate_format(
        "{'key1': 'value1', 'key2': [1, 2, 3], 'key3': (1, 2, 3)}"))
    print(validate_format(
        "{'key1': ['value1', 'key2': [1, 2, 3], 'key3': (1, 2, 3)}"))
    print(validate_format("{"))
    print(validate_format("]"))
    print(validate_format("{[}]"))
