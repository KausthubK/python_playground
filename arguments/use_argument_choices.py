import argparse

ASTR = "a string"
BSTR = "b string"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run test job for pipeline 1")
    parser.add_argument(
        "--val",
        default=ASTR,
        choices=[ASTR, BSTR],
    )
    args = parser.parse_args()
    print(args.val)
