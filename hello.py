"""my-project 示例主程序。

运行方式：
    python hello.py
"""

from utils import greet, summarize


def main() -> None:
    name = "WorkBuddy"
    print(greet(name))

    numbers = [4, 7, 1, 9, 3, 7]
    print(summarize(numbers))


if __name__ == "__main__":
    main()
