# let's add the "item" to the list "ls"
def my_append(item, ls = []):
    ls.append(item)


def is_same_set(values, order):
    return sorted(list(set(values))) == set(order)


def do_something(value: int):
    if value < 0:
        ValueError("Please enter a positive number")
    elif value == 42:
        raise "42 is forbidden"
    print(f"Your number is: {value}")


def iterating_only_once(cond, cond2):
    while cond:
        if cond2:
            break
        else:
            break


def infinite_recursion():
    return [x + 1 for x in infinite_recursion()]
