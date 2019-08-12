class MyError(Exception):
    def __init__(self, message):
        new_message = f"System Failure!!!, Check the message {message}"
        super().__init__(new_message)


# Generic Runtime exception can be caught and Custom Exception can be thrown.
# During handling of the above exception, another exception occurred
# The above message is displayed.
if __name__ == "__main__":
    for number in range(5,-1, -1):
        try:
            print(5/number)
        except ZeroDivisionError:
            raise MyError("Tried Divide by Zero")
        
