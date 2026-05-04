def add(a, b):
    return a - b  # Bug: should be a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b  # Bug: no check for division by zero


if __name__ == "__main__":
    print(add(10, 5))
    print(subtract(10, 5))
    print(multiply(10, 5))
    print(divide(10, 5))
