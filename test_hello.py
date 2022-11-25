from hello import toyou, add, subtract


def setup_function(function):
    print(f" Running Setup: {function.__name__}")
    function.x = 10


def teardown_function(function):
    print(f" Running Teardown: {function.__name__}")
    del function.x


def test_add():
    assert add(test_add.x) == 11


def test_subtract():
    assert subtract(test_subtract.x) == 9
