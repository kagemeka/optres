# mypy: ignore-errors
import unittest
from dataclasses import dataclass
from typing import TypeVar, cast

from .option import unwrap

T = TypeVar("T")
E = TypeVar("E", bound=Exception)
U = TypeVar("U")


def is_ok(x: U) -> bool:
    return not is_err(x)


def is_err(x: U) -> bool:
    return isinstance(x, Exception)


def ok(x: U) -> T | None:
    return cast(T, x) if is_ok(x) else None


def err(x: U) -> E | None:
    return cast(E, x) if is_err(x) else None


def unwrap_ok(x: T | E) -> T:
    return unwrap(ok(x))


def unwrap_err(x: T | E) -> E:
    return unwrap(err(x))


class _Tests(unittest.TestCase):
    def test(self) -> None:
        @dataclass
        class NegativeError(Exception):
            value: int

        def be_positive(x: int) -> int | NegativeError:
            return x if x >= 0 else NegativeError(x)

        assert is_ok(be_positive(0))
        a = be_positive(-1)
        assert is_err(a)
        assert ok(a) is None
        assert err(a) == NegativeError(-1)
        assert unwrap_err(a).value == -1


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
