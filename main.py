import os

PATH_TO_BOOKS = "books/"

def main():
    books = [f"{PATH_TO_BOOKS}{book}" for book in os.listdir(PATH_TO_BOOKS)]
    for book in books:
        with open(book,'r') as bfile:
            contents = bfile.read()
            print(contents)


if __name__ == "__main__":
    main()
