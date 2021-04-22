Generators
============

Dataclass Bakery has different generators to generate data depending on the dataclass attributes typing, we are working to develop more generators, but now we have these:

Bool Generator
---------------

`from dataclass_bakery.generators.random_bool_generator import RandomBoolGenerator`

Generator for random `bool`, for example:

- Attribute example:

::

    is_safe: bool

- The bool generator generate: `True`


Defaults: Does not have


Complex Generator
------------------

`from dataclass_bakery.generators.random_complex_generator import RandomComplexGenerator`

Generator for a random `complex` number, for example:

- Attribute example:

::

    price: complex

- The complex generator generate: `(1.3+5.2j)`


Defaults: 

    - _min_limit_ = 0 (Minimun limit of the real and imaginary part) 
    - _max_limit_ = 100 (Maximun limit of the real and imaginary part)
    - _decimals_ = 2 (Maximum figures of the decimal part)


Decimal Generator
------------------

`from dataclass_bakery.generators.random_decimal_generator import RandomDecimalGenerator`

Generator for a `Decimal` number (from decimal import Decimal), for example:

- Attribute example:

::

    price: Decimal

- The Decimal generator generate: `Decimal('1.2')`


Defaults: 

    - _min_limit_ = 0 (Minimun limit of the number) 
    - _max_limit_ = 100 (Maximun limit of the number)
    - _decimals_ = 2 (Maximum figures of the decimal part)


Dict Generator
------------------

`from dataclass_bakery.generators.random_dict_generator import RandomDictGenerator`

Generator for a `dict` or a `Dict` (from typing import Dict), for example:

- Attributes example:

::

    first_dict: dict
    second_dict: Dict[str, int]

- The dict generator generate in both cases: `{"key1": 1, "key2": 2}`

Defaults: 

    - _max_length_ = 2 (Length of the generated dict) 
    - _default_key_type_ = str (Typing of the keys in the generated dict, if you don't specify with Dict[])
    - _default_value_type_ = int (Typing of the values in the generated dict, if you don't specify with Dict[])


Float Generator
------------------

`from dataclass_bakery.generators.random_float_generator import RandomFloatGenerator`

Generator for a `float` number, for example:

- Attribute example:

::

    price: float

- The float generator generate: `1.2`


Defaults: 

    - _min_limit_ = 0 (Minimun limit of the number) 
    - _max_limit_ = 100 (Maximun limit of the number)
    - _decimals_ = 2 (Maximum figures of the decimal part)


Integer Generator
------------------

`from dataclass_bakery.generators.random_int_generator import RandomIntGenerator`

Generator for an `int` number, for example:

- Attribute example:

::

    age: int

- The integer generator generate: `1`


Defaults: 

    - _min_limit_ = 0 (Minimun limit of the number) 
    - _max_limit_ = 100 (Maximun limit of the number)


List Generator
------------------

`from dataclass_bakery.generators.random_list_generator import RandomListGenerator`

Generator for a `list` or a `List` (from typing import List), for example: 

- Attributes example:

::

    first_list: list
    second_list: List[int]

- The list generator generate in both cases: `[1, 2]`


Default values: 

    - _max_length_ = 2 (Length of the generated list) 
    - _default_value_type_ = int (Typing of the values in the generated list, if you don't specify with List[])


Option Generator
------------------

`from dataclass_bakery.generators.random_option_generator import RandomOptionGenerator`

Generator for a `Literal` (from typing import Literal), for example:


- Attribute example:

::

    stuff: Literal["a", "b", "c"]

- The option generator generate: `"b"`


Defaults: Does not have


Range Generator
------------------

`from dataclass_bakery.generators.random_range_generator import RandomRangeGenerator`

Generator for a `range`, for example:

- Attribute example:

::

    price_range: range

- The range generator generate: `range(20, 38)`


Defaults: 

    - _min_limit_ = 0 (Minimun limit of the range) 
    - _max_limit_ = 100 (Maximun limit of the range)


Set Generator
------------------

`from dataclass_bakery.generators.random_set_generator import RandomSetGenerator`

Generator for a `set`, for example: 

- Attributes:

::

    first_set: set

- The set generator generate in both cases: `{1, 2}`


Default values: 

    - _max_length_ = 2 (Length of the generated set) 
    - _default_value_type_ = int (Typing of the values in the generated set)


String Generator
------------------

`from dataclass_bakery.generators.random_str_generator import RandomStrGenerator`

Generator for an `str`, for example:

- Attribute example:

::

    name: str

- The string generator generate: ``


Defaults: 

    - _max_length_ = 2 (Length of the generated string)


Tuple Generator
------------------

`from dataclass_bakery.generators.random_tuple_generator import RandomTupleGenerator`

Generator for a `tuple` or a `Tuple` (from typing import Tuple), for example: 

- Attributes example:

::

    first_tuple: tuple
    second_tuple: Tuple[int]

- The tuple generator generate: `(1, 2)`


Default values: 

    - _max_length_ = 2 (Length of the generated tuple) 
    - _default_value_type_ = int (Typing of the values in the generated tuple if you don't specify with Tuple[])


UUID Generator
---------------

`from dataclass_bakery.generators.random_uuid_generator import RandomUuidGenerator`

Generator for an `UUID`

- Attribute example:

::

    id: UUID

- The uuid generator generate: `UUID('18f04f72-a563-495c-af5c-f5286c649fc9')`


Defaults: Does not have
