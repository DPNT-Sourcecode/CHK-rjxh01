

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    if type(friend_name) != str:
        raise TypeError("Expected a string")
    return "Hello World"


