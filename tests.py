from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.write_file import write_file


def test_get_files_info():
    result = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(result)
    print("")

    result = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(result)
    print("")

    result = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(result)
    print("")

    result = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(result)
    print("")


def test_get_file_content():
    result = get_file_content("calculator", "lorem.txt")
    print("Result for 'lorem.txt' file:")
    print(result)
    print("")

    result = get_file_content("calculator", "main.py")
    print("Result for 'main.py' file:")
    print(result)
    print("")

    result = get_file_content("calculator", "pkg/calculator.py")
    print("Result for 'pkg/calculator.py' file:")
    print(result)
    print("")

    result = get_file_content("calculator", "/bin/cat")
    print("Result for '/bin/cat' file:")
    print(result)
    print("")


def test_write_file():
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print("Result for writing to 'lorem.txt':")
    print(result)
    print("")

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("Result for writing to 'pkg/morelorem.txt':")
    print(result)
    print("")

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("Result for writing to '/tmp/temp.txt':")
    print(result)
    print("")


def test():
    test_write_file()


if __name__ == "__main__":
    test()
