def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)

def test_exception_was_raised(func, args, message):
    """
    This test takes a function, arguments and a message as arguments. It can be
    used to test if the exception is raised and the correct message is thrown.
    """
    try:
        func(*args)
        assert False, "Exception was not raised."
    except Exception as e:
        assert e.args[0] == message, "The message that was provided did not match the message thrown."
