import os

from dotenv import load_dotenv


def main():
    load_dotenv(".env", override=True)

    print("Hello from langchain-course!")


if __name__ == "__main__":
    main()
