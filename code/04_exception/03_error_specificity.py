import math

# The order of exception should be specific to general


def division(num):
    try:
        result = math.pi / num
    except ArithmeticError as ex:  # General Exception
        print("Arithemetic Error: ", ex)
        # Bad except clauses order (ArithmeticError is an ancestor class of ZeroDivisionError)
    except ZeroDivisionError as ex:  # Specific Exception
        print("ZeroDivisionError: ", ex)
    else:  # No exception occurs then execute this else block.
        return result


def good_division(num):
    try:
        my_result = math.pi / num
    except ZeroDivisionError as ex:
        print("Zero Division Error: ", ex)
    except ArithmeticError as ex:
        print("ArithmeticError ", ex)
    else:
        return my_result


# Do not catch generic exception.
def never_do_this():
    try:
        int("a")
    except Exception:
        pass


if __name__ == "__main__":
    division(0)
    good_division(0)
    never_do_this()
