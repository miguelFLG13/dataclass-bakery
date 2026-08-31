from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Literal, NamedTuple, Optional, Tuple, TypedDict, Union


class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


class Point(NamedTuple):
    x: int
    y: int


class Payload(TypedDict):
    name: str
    age: int


@dataclass
class Stuff:
    id: int


@dataclass
class StuffNested1:
    item: Stuff


@dataclass
class StuffNested2:
    item: StuffNested1


@dataclass
class StuffList:
    item_list: List[str]


@dataclass
class StuffTuple:
    item_tuple: Tuple[str]


@dataclass
class StuffDict:
    item_dict: Dict[float, complex]


@dataclass
class StuffUnion:
    item_union: Union[float, complex]


@dataclass
class StuffOptional:
    item_optional: Optional[float]


@dataclass
class StuffLiteral:
    item_literal: Literal["a", "s", "d"]


@dataclass
class StuffEnum:
    item_enum: Color


@dataclass
class StuffOptionalEnum:
    item_optional_enum: Optional[Color]


@dataclass
class StuffMultiUnion:
    item_multi_union: Union[int, str, float]


@dataclass
class StuffNestedList:
    item_nested_list: List[List[int]]


@dataclass
class StuffNestedDict:
    item_nested_dict: Dict[str, List[int]]


@dataclass
class StuffNamedTuple:
    item_named_tuple: Point


@dataclass
class StuffTypedDict:
    item_typed_dict: Payload
