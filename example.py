from dataclasses import dataclass, fields
from datetime import date, datetime, time, timedelta
from decimal import Decimal
from enum import Enum
from fractions import Fraction
from ipaddress import IPv4Address, IPv6Address
from pathlib import Path
from typing import (
    Counter as TCounter, DefaultDict, Deque, Dict, FrozenSet, List,
    Literal, NamedTuple, Optional, Set, Tuple, Type, TypedDict, Union,
)
from uuid import UUID
from zoneinfo import ZoneInfo

from dataclass_bakery import baker


class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


class Point(NamedTuple):
    x: int
    y: int


class Address(TypedDict):
    city: str
    zip_code: int


@dataclass
class Company:
    name: str
    employees: int


@dataclass
class Everything:
    # Scalars
    field_str: str
    field_int: int
    field_float: float
    field_complex: complex
    field_bool: bool
    field_bytes: bytes
    field_bytearray: bytearray

    # Date and time
    field_date: date
    field_datetime: datetime
    field_time: time
    field_timedelta: timedelta

    # Special numeric types
    field_decimal: Decimal
    field_fraction: Fraction

    # Identifiers / networking
    field_uuid: UUID
    field_path: Path
    field_ipv4: IPv4Address
    field_ipv6: IPv6Address
    field_zoneinfo: ZoneInfo

    # Native containers
    field_range: range
    field_list: list
    field_tuple: tuple
    field_dict: dict
    field_set: set
    field_frozenset: frozenset

    # typing containers (parametrized)
    field_List: List[int]
    field_Tuple: Tuple[str]
    field_Dict: Dict[str, int]
    field_Set: Set[int]
    field_FrozenSet: FrozenSet[int]
    field_Deque: Deque[int]
    field_Counter: TCounter[str]
    field_DefaultDict: DefaultDict[str, int]

    # Advanced typing
    field_literal: Literal["a", "b", "c"]
    field_enum: Color
    field_type: Type[int]
    field_union: Union[int, str, float]
    field_optional: Optional[str]

    # Nested types
    field_nested_dataclass: Company
    field_named_tuple: Point
    field_typed_dict: Address
    field_nested_list: List[List[int]]
    field_nested_dict: Dict[str, List[int]]


obj = baker.make(Everything)

print(repr(obj))
print()
print(f"{'field':<26} {'type':<16} value")
print("-" * 80)
for f in fields(obj):
    value = getattr(obj, f.name)
    print(f"{f.name:<26} {type(value).__name__:<16} {value!r}")
