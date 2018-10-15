
class Test:

    def __init__(self):
        self.value = 0

    def __enter__(self):
        print("enter!")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_val)
        print("exit!")


class MyException(Exception):
    pass


def show_message(message):
    raise MyException(message)


if __name__ == "__main__":

    t = Test()

    with t:
        # show_message("Hello!!!")
        print("Hello!")

