# Dataclass Bakery
Dataclass Bakery offers you a smart way to create objects based on dataclasses for testing in Python.
Inspired in model bakery module for Django.

> **This is the same `dataclass-bakery` project.** It was originally published on PyPI as `dataclass-bakery`, but access to that original PyPI account/project was lost, so it is now published as `dataclass-bakery2` and will keep evolving under this new name starting from this version onwards. Nothing else changes: it's the same codebase, same maintainer, same repository — only the PyPI distribution name is different.

### Install

`pip install dataclass-bakery2`

> Note: the PyPI distribution is named `dataclass-bakery2`, but the importable module is still `dataclass_bakery` (see the usage example below).

### Usage and Info

#### Basic usage

```
from dataclasses import dataclass

from dataclass_bakery import baker


@dataclass
class Customer:
    id: int
    name: str
    spent_money: float
    
    
baker.make(Customer)
baker.make(Customer, _quantity=3)

"""
Customer(id=25, name='vzWoIfgoZM', spent_money=16.36)

[Customer(id=27, name='OYvyWakmUX', spent_money=84.98), Customer(id=41, name='AiancdsmLg', spent_money=57.57), Customer(id=92, name='feTxLyuSus', spent_money=26.06)]
"""
```

For more information: https://dataclass-bakery.readthedocs.io/

#### Types available:

 - int
 - str
 - float
 - bool
 - complex
 - bytes
 - bytearray
 - date
 - datetime (optionally timezone-aware with `_tz_aware_`)
 - time (optionally timezone-aware with `_tz_aware_`)
 - timedelta
 - range
 - list / List (from typing import List)
 - tuple / Tuple (from typing import Tuple)
 - dict / Dict (from typing import Dict)
 - set / Set (from typing import Set)
 - frozenset / FrozenSet (from typing import FrozenSet)
 - deque / Deque (from collections import deque, from typing import Deque)
 - OrderedDict (from collections import OrderedDict, or from typing import OrderedDict)
 - Counter (from collections import Counter, or from typing import Counter)
 - defaultdict / DefaultDict (from collections import defaultdict, from typing import DefaultDict)
 - Path (from pathlib import Path)
 - Decimal (from decimal import Decimal)
 - Fraction (from fractions import Fraction)
 - UUID (from uuid import UUID)
 - IPv4Address / IPv6Address (from ipaddress import IPv4Address, IPv6Address)
 - ZoneInfo (from zoneinfo import ZoneInfo)
 - Enum (any subclass: Enum, IntEnum, StrEnum, Flag, IntFlag...)
 - Literal (from typing import Literal)
 - Type / type (from typing import Type)
 - Union (from typing import Union) — picks a random member among all the non-`None` options
 - Optional (from typing import Optional)
 - any nested dataclass, `typing.NamedTuple` or `typing.TypedDict`
 - any of the above **nested** inside a container, e.g. `List[List[int]]` or `Dict[str, List[int]]`

All container types work the same way with their native form (`dict`) or their `typing` equivalent, bare or parametrized (`Dict`, `Dict[str, int]`), and with the modern `list[int]` / `int | None` syntax.
