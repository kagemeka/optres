import unittest
from dataclasses import dataclass
from typing import Generic, TypeVar, Union, cast, final

from .option_v2 import Option, Some, unwrap

T = TypeVar("T", contravariant=True)
E = TypeVar("E", contravariant=True)
U = TypeVar("U", covariant=True)


@final
@dataclass(frozen=True)
class Ok(Generic[T]):
    value: T


@final
@dataclass(frozen=True)
class Err(Generic[E]):
    value: E


Result = Union[Ok[T], Err[E]]


def is_ok(x: Result[T, E]) -> bool:
    return isinstance(x, Ok)


def is_err(x: Result[T, E]) -> bool:
    return isinstance(x, Err)


def ok(x: Result[T, E]) -> Option[T]:
    return Some(cast(Ok[T], x).value) if is_ok(x) else None


def err(x: Result[T, E]) -> Option[E]:
    return Some(cast(Err[E], x).value) if is_err(x) else None


def unwrap_ok(x: Result[U, E]) -> U:
    return unwrap(ok(x))


def unwrap_err(x: Result[T, U]) -> U:
    return unwrap(err(x))


class _Tests(unittest.TestCase):
    def test(self) -> None:
        def generate_error() -> Result[int, str]:
            return Err("nothing")

        a = Err(1)
        assert not is_ok(a)
        assert ok(a) is None
        assert err(a) == Some(1)
        assert is_err(generate_error())
        assert unwrap_err(generate_error()) == "nothing"


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
