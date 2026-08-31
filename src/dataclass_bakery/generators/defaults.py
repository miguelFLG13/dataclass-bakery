from collections import Counter, OrderedDict, defaultdict, deque
from datetime import date, datetime, time, timedelta
from decimal import Decimal
from enum import Enum
from fractions import Fraction
from ipaddress import IPv4Address, IPv6Address
from pathlib import Path
from typing import Literal
from uuid import UUID
from zoneinfo import ZoneInfo

from dataclass_bakery.generators.random_bool_generator import RandomBoolGenerator
from dataclass_bakery.generators.random_bytearray_generator import (
    RandomBytearrayGenerator,
)
from dataclass_bakery.generators.random_bytes_generator import RandomBytesGenerator
from dataclass_bakery.generators.random_complex_generator import RandomComplexGenerator
from dataclass_bakery.generators.random_counter_generator import RandomCounterGenerator
from dataclass_bakery.generators.random_date_generator import RandomDateGenerator
from dataclass_bakery.generators.random_datetime_generator import (
    RandomDatetimeGenerator,
)
from dataclass_bakery.generators.random_decimal_generator import RandomDecimalGenerator
from dataclass_bakery.generators.random_defaultdict_generator import (
    RandomDefaultdictGenerator,
)
from dataclass_bakery.generators.random_deque_generator import RandomDequeGenerator
from dataclass_bakery.generators.random_dict_generator import RandomDictGenerator
from dataclass_bakery.generators.random_enum_generator import RandomEnumGenerator
from dataclass_bakery.generators.random_float_generator import RandomFloatGenerator
from dataclass_bakery.generators.random_fraction_generator import (
    RandomFractionGenerator,
)
from dataclass_bakery.generators.random_frozenset_generator import (
    RandomFrozensetGenerator,
)
from dataclass_bakery.generators.random_int_generator import RandomIntGenerator
from dataclass_bakery.generators.random_ipv4_generator import RandomIpv4Generator
from dataclass_bakery.generators.random_ipv6_generator import RandomIpv6Generator
from dataclass_bakery.generators.random_list_generator import RandomListGenerator
from dataclass_bakery.generators.random_option_generator import RandomOptionGenerator
from dataclass_bakery.generators.random_ordered_dict_generator import (
    RandomOrderedDictGenerator,
)
from dataclass_bakery.generators.random_path_generator import RandomPathGenerator
from dataclass_bakery.generators.random_range_generator import RandomRangeGenerator
from dataclass_bakery.generators.random_set_generator import RandomSetGenerator
from dataclass_bakery.generators.random_str_generator import RandomStrGenerator
from dataclass_bakery.generators.random_time_generator import RandomTimeGenerator
from dataclass_bakery.generators.random_timedelta_generator import (
    RandomTimedeltaGenerator,
)
from dataclass_bakery.generators.random_tuple_generator import RandomTupleGenerator
from dataclass_bakery.generators.random_type_generator import RandomTypeGenerator
from dataclass_bakery.generators.random_uuid_generator import RandomUuidGenerator
from dataclass_bakery.generators.random_zoneinfo_generator import (
    RandomZoneinfoGenerator,
)

# Generators
TYPING_GENERATORS = {
    str: RandomStrGenerator,
    int: RandomIntGenerator,
    float: RandomFloatGenerator,
    complex: RandomComplexGenerator,
    bool: RandomBoolGenerator,
    dict: RandomDictGenerator,
    list: RandomListGenerator,
    tuple: RandomTupleGenerator,
    set: RandomSetGenerator,
    frozenset: RandomFrozensetGenerator,
    range: RandomRangeGenerator,
    date: RandomDateGenerator,
    datetime: RandomDatetimeGenerator,
    time: RandomTimeGenerator,
    timedelta: RandomTimedeltaGenerator,
    Decimal: RandomDecimalGenerator,
    Fraction: RandomFractionGenerator,
    Path: RandomPathGenerator,
    UUID: RandomUuidGenerator,
    Literal: RandomOptionGenerator,
    Enum: RandomEnumGenerator,
    bytes: RandomBytesGenerator,
    bytearray: RandomBytearrayGenerator,
    IPv4Address: RandomIpv4Generator,
    IPv6Address: RandomIpv6Generator,
    deque: RandomDequeGenerator,
    OrderedDict: RandomOrderedDictGenerator,
    Counter: RandomCounterGenerator,
    defaultdict: RandomDefaultdictGenerator,
    type: RandomTypeGenerator,
    ZoneInfo: RandomZoneinfoGenerator,
}

# Generator Default Values
NUMBER_MIN_LIMIT = 0
NUMBER_MAX_LIMIT = 100

DECIMALS = 2


HOUR_MIN_LIMIT = 0
HOUR_MAX_LIMIT = 23
MINUTE_MIN_LIMIT = 0
MINUTE_MAX_LIMIT = 59
SECOND_MIN_LIMIT = 0
SECOND_MAX_LIMIT = 59
DAY_MIN_LIMIT = 1
DAY_MAX_LIMIT = 28
MONTH_MIN_LIMIT = 1
MONTH_MAX_LIMIT = 12
YEAR_MIN_LIMIT = 2000
YEAR_MAX_LIMIT = 2100

DEFAULT_KEY_TYPE = str
DEFAULT_VALUE_TYPE = int
DEFAULT_PATH_TYPE = str

MAX_STR_LENGTH = 10
MAX_LIST_LENGTH = 2
MAX_TUPLE_LENGTH = 2
MAX_SET_LENGTH = 2
MAX_DICT_LENGTH = 2
MAX_PATH_LENGTH = 2
MAX_BYTES_LENGTH = 10
MAX_BYTEARRAY_LENGTH = 10
MAX_FROZENSET_LENGTH = 2
MAX_DEQUE_LENGTH = 2
MAX_ORDERED_DICT_LENGTH = 2
MAX_COUNTER_LENGTH = 2
MAX_DEFAULTDICT_LENGTH = 2

TIMEDELTA_DAYS_MIN_LIMIT = 0
TIMEDELTA_DAYS_MAX_LIMIT = 365

FRACTION_DENOMINATOR_MIN_LIMIT = 1
FRACTION_DENOMINATOR_MAX_LIMIT = 100

# Bakery Arguments
FIXED_VALUE_ARG = "_fixed_value_"  # A value to directly assig to the attr
GENERATOR_ARG = "_generator_"  # Generator to change the default generator
KEY_TYPE_ARG = "_key_type_"  # Key type in a dict
VALUE_TYPE_ARG = "_value_type_"  # Value type in a list, tuple or dict
OPTIONS_ARG = "_options_"  # Options in RandomOptionGenerator
NUMBER_MIN_LIMIT_ARG = "_min_limit_"  # Fix a min limit of a number
NUMBER_MAX_LIMIT_ARG = "_max_limit_"  # Fix a max limit of a number
DECIMALS_ARG = "_decimals_"  # Fix how many decimals has a number
MAX_LENGTH_ARG = "_max_length_"  # Fix length in a attr
DEFAULT_KEY_TYPE_ARG = "_default_key_type_"  # Fix the default key typing
DEFAULT_VALUE_TYPE_ARG = "_default_value_type_"  # Fix the default value typing
HOUR_MIN_LIMIT_ARG = "_min_hour_limit_"
HOUR_MAX_LIMIT_ARG = "_max_hour_limit_"
MINUTE_MIN_LIMIT_ARG = "_min_minute_limit_"
MINUTE_MAX_LIMIT_ARG = "_max_minute_limit_"
SECOND_MIN_LIMIT_ARG = "_min_second_limit_"
SECOND_MAX_LIMIT_ARG = "_max_second_limit_"
DAY_MIN_LIMIT_ARG = "_min_day_limit_"
DAY_MAX_LIMIT_ARG = "_max_day_limit_"
MONTH_MIN_LIMIT_ARG = "_min_month_limit_"
MONTH_MAX_LIMIT_ARG = "_max_month_limit_"
YEAR_MIN_LIMIT_ARG = "_min_year_limit_"
YEAR_MAX_LIMIT_ARG = "_max_year_limit_"
IGNORE_ARG = "_ignore_"
TIMEDELTA_DAYS_MIN_LIMIT_ARG = "_min_timedelta_days_limit_"
TIMEDELTA_DAYS_MAX_LIMIT_ARG = "_max_timedelta_days_limit_"
FRACTION_DENOMINATOR_MIN_LIMIT_ARG = "_min_denominator_limit_"
FRACTION_DENOMINATOR_MAX_LIMIT_ARG = "_max_denominator_limit_"
ENUM_CLASS_ARG = "_enum_class_"  # Enum class to pick a random member from
TZ_AWARE_ARG = "_tz_aware_"  # Attach a random IANA timezone to a time/datetime
