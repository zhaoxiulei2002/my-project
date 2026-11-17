"""示例工具函数。"""


def greet(name: str) -> str:
    """返回一条问候语。"""
    return f"Hello, {name}! Welcome to my-project."


def summarize(numbers: list[int]) -> str:
    """返回一组数字的简单统计信息。"""
    if not numbers:
        return "No numbers provided."
    return (
        f"count={len(numbers)}, "
        f"min={min(numbers)}, "
        f"max={max(numbers)}, "
        f"sum={sum(numbers)}"
    )
