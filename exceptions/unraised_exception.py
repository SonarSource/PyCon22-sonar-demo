def do_something(value: int):
    if value < 0:
        ValueError("Please enter a positive number")
    elif value == 42:
        raise "42 is forbidden"
    print(f"Your number is: {value}")


