def greet(*names):
    """ Python Arbitrary Arguments - This function greets all
    the person in the names tuple."""

    for name in names:
        print("Hello", name)


greet("Monica", "Luke", "Steve", "John")
