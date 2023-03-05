import unittest
from typing import Generic, NoReturn, TypeVar, Union, final

T = TypeVar("T")


@final
class Ok(Generic[T]):
    value: T

    def __init__(self, value: T) -> None:
        self.value = value

    @property
    def is_ok(self) -> bool:
        return True

    @property
    def is_err(self) -> bool:
        return False

    def unwrap_ok(self) -> T:
        return self.value

    def unwrap_err(self) -> NoReturn:
        raise NotImplementedError


E = TypeVar("E")


@final
class Err(Generic[E]):
    value: E

    def __init__(self, value: E) -> None:
        self.value = value

    @property
    def is_ok(self) -> bool:
        return False

    @property
    def is_err(self) -> bool:
        return True

    def unwrap_ok(self) -> NoReturn:
        raise NotImplementedError

    def unwrap_err(self) -> E:
        return self.value


Result = Union[Ok[T], Err[E]]


class _Tests(unittest.TestCase):
    def test(self) -> None:
        def generate_error() -> Result[int, str]:
            return Err("nothing")

        a = Err(1)
        assert not a.is_ok
        assert generate_error().is_err
        assert generate_error().unwrap_err() == "nothing"


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
