from typing import LiteralString

from optres import Err, Result, is_err, is_ok, unwrap, unwrap_err


def return_result(x: int | None) -> Result[int, LiteralString]:
    return Err("not int") if x is None else x


def example() -> None:
    a: int | None = 1
    c: int = unwrap(a)
    print(c)
    assert is_ok(return_result(a))
    a = None
    # unwrap(a) # error := panic in Rust.
    may_be_err = return_result(a)
    assert is_err(may_be_err)
    print(unwrap_err(may_be_err))


if __name__ == "__main__":
    example()
