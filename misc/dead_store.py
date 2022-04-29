def my_dead_store():
    x = 42
    ...
    x = 24
    print(x)


def my_overriden_param(elem, my_list):
    for elem in my_list:
        print(elem)
