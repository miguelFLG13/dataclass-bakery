from decimal import Decimal
from pathlib import Path

from dataclass_bakery.generators.random_bool_generator import RandomBoolGenerator
from dataclass_bakery.generators.random_complex_generator import RandomComplexGenerator
from dataclass_bakery.generators.random_decimal_generator import RandomDecimalGenerator
from dataclass_bakery.generators.random_dict_generator import RandomDictGenerator
from dataclass_bakery.generators.random_float_generator import RandomFloatGenerator
from dataclass_bakery.generators.random_int_generator import RandomIntGenerator
from dataclass_bakery.generators.random_list_generator import RandomListGenerator
from dataclass_bakery.generators.random_path_generator import RandomPathGenerator
from dataclass_bakery.generators.random_range_generator import RandomRangeGenerator
from dataclass_bakery.generators.random_str_generator import RandomStrGenerator
from dataclass_bakery.generators.random_tuple_generator import RandomTupleGenerator


TYPING_GENERATORS = {
    str: RandomStrGenerator,
    int: RandomIntGenerator,
    float: RandomFloatGenerator,
    complex: RandomComplexGenerator,
    bool: RandomBoolGenerator,
    dict: RandomDictGenerator,
    list: RandomListGenerator,
    tuple: RandomTupleGenerator,
    range: RandomRangeGenerator,
    Decimal: RandomDecimalGenerator,
    Path: RandomPathGenerator,
}

NUMBER_MIN_LIMIT = 0
NUMBER_MAX_LIMIT = 100

DECIMALS = 2

DEFAULT_KEY_TYPE = str
DEFAULT_VALUE_TYPE = int
DEFAULT_PATH_TYPE = str

MAX_STR_LENGTH = 10
MAX_LIST_LENGTH = 3
MAX_TUPLE_LENGTH = 3
MAX_DICT_LENGTH = 3
MAX_PATH_LENGTH = 5
