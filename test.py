# test.py

from qrio import encode, decode

def main() -> None:
    """A function to run the main test."""

    data = "hello world"

    print(data == decode(encode(data.encode())).decode())

if __name__ == "__main__":
    main()
