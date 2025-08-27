import time


def foo():
    time.sleep(1)
    print("Function foo executed")


def bar():
    time.sleep(2)
    print("Function bar executed")


def main():
    foo()
    bar()


if __name__ == "__main__":
    main()
