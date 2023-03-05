import unittest
from dataclasses import dataclass
from typing import Generic, TypeVar, Union, final

T = TypeVar("T")


@final
@dataclass(frozen=True)
class Some(Generic[T]):
    value: T


Option = Union[Some[T], None]


def unwrap(x: Option[T]) -> T:
    assert x is not None
    return x.value


class _Tests(unittest.TestCase):
    def test(self) -> None:
        def receive_int(b: int) -> None:
            ...

        a: Option[int] = Some(1)

        receive_int(unwrap(a))


if __name__ == "__main__":
    import doctest

    unittest.main()

    doctest.testmod(verbose=True)
