import Refactoring as main


def test_hello_world() -> None:
    hello = main.hello_world()
    assert hello == "Hello World"
