from pydantic import validate_arguments

@validate_arguments
def foo(x: int, y: str):
    for _ in range(x):
        print(y)


if __name__ == "__main__":
    foo(3, "hello")
    # foo(3, 4)