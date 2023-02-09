
# optres

`Yet another Rust's Option<T> and Result<T, E> simple implementation in Python.`

[![Python package][ci-badge]][ci-url]
[![PyPI version][pypi-badge]][pypi-url]
[![License: MIT][license-badge]][license-url]
[![pre-commit][pre-commit-badge]][pre-commit-url]
[![Github pages][gh-pages-badge]][gh-pages-url]

[ci-badge]: https://github.com/kagemeka/optres/actions/workflows/ci.yml/badge.svg
[ci-url]: https://github.com/kagemeka/optres/actions/workflows/ci.yml
[pre-commit-badge]: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
[pre-commit-url]: https://github.com/pre-commit/pre-commit
[license-badge]: https://img.shields.io/badge/License-Apache2.0-green.svg
[license-url]: https://opensource.org/licenses/Apache2.0
[pypi-badge]: https://badge.fury.io/py/optres.svg
[pypi-url]: https://badge.fury.io/py/optres
[gh-pages-badge]: https://github.com/kagemeka/optres/actions/workflows/pages/pages-build-deployment/badge.svg
[gh-pages-url]: https://kagemeka.github.io/optres

## Installation

```bash
python3 -m pip install -U optres
```

## Example

```py
from optres import unwrap, Result, Err, is_ok, is_err, unwrap_err
from typing import LiteralString


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

```
