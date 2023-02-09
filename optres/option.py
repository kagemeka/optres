"""
this module is inspired by Rust.
there is already Optional[T] type in Python.
Optional[T] = Union[T, None] = T | None
:= enum Option<T>{ Some(T), None } in Rust.
Rust's Option<T> type has many methods on its own.
however in Python, we cannot implement additional method on std type.
farthermore, below inheritance is invalid in Python.
Optional[T] cannot be inherited.
class Option(Optional[T]):
    ...

so we decide to implement Option<T> functinalities as function in Python.
"""

import unittest
from typing import TypeVar

T = TypeVar("T")


def unwrap(x: T | None) -> T:
    assert x is not None
    return x


class _Tests(unittest.TestCase):
    def test(self) -> None:
        def receive_int(b: int) -> None:
            ...

        a: int | None = 1

        receive_int(unwrap(a))


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
