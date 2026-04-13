"""String and stack-like helpers."""


def is_valid_brackets(text: str) -> bool:
    pairs = {")": "(", "]": "[", "}": "{"}
    stack: list[str] = []

    for char in text:
        if char in "([{":
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False

    return len(stack) == 0


def jewel_count(jewels: str, stones: str) -> int:
    unique_jewels = set(jewels)
    return sum(1 for stone in stones if stone in unique_jewels)
