from dataclasses import dataclass
from typing import Dict, List, Literal, Optional, Tuple, Union


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
