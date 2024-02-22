Custom Objects
===============

Sometimes, probably, you need more power to give details to the generated objects, no problem, Dataclass bakery helps you to generate that special environment you need to test your code using the `_default_attrs` argument in the baker.

We are working with two dataclasses, `Customer` and `Address`:

::

    from dataclasses import dataclass
    from typing import List, Optional
    from uuid import UUID


    @dataclass
    class Customer:
        id: int
        name: str
        spent_money: float
        address: Address
        orders: List[UUID]
        
        
    @dataclass
    class Address
        street_name: str
        number: Optional[int]


To change the behaviour with the default values of the baker we need to type:

::

    from dataclass_bakery import baker

    defaults = {
        'street_name': {
            '_max_length_': 15
        }
    }

    baker.make(Address, _attr_defaults=defaults)

    """
    Address(street_name='vnlHYKsDXQkyODI', number=49)
    """

You can read the default values you can change per generator in the generators page.

Also you can change the generator of an attribute:

::

    from dataclass_bakery.generators.random_str_generator import RandomStrGenerator

    defaults = {
        'number': {
            '_generator_': RandomStrGenerator
        }
    }

    baker.make(Address, _attr_defaults=defaults)

    """
    Address(street_name='RtfgQkyODI', number='KsDXQkyODI')
    """

Another possibility is fix a value:

::

    defaults = {
        'number': {
            '_fixed_value_': 1234
        }
    }

    baker.make(Address, _attr_defaults=defaults)

    """
    Address(street_name='jdRFDadkXf', number=1234)
    """

And you can combine some different actions in your generated object:

::

    from dataclass_bakery.generators.random_float_generator import RandomFloatGenerator

    defaults = {
        'number': {
            '_generator_': RandomFloatGenerator,
            '_min_limit_': 30
        },
        'street_name': {
            '_max_length_': 20
        }
    }

    baker.make(Address, _attr_defaults=defaults)

    """
    Address(number=42.93, street_name='YqgpvEISVKzAlfeemJil')
    """


Finally you can do all actions you read before in different data class levels:

::

    defaults = {
        'name': {
            '_max_length_': 20
        },
        'address': {
            'number': {
                '_generator_': RandomFloatGenerator,
                '_min_limit_': 30
            },
            'street_name': {
                '_max_length_': 20
            }
        }
    }

    baker.make(Customer, _attr_defaults=defaults)

    """
    Customer(id=16, name='MRoWdUYJiKbFddoCbeOm', spent_money=23.88, address=Address(number=48.34, street_name='qRRXWiUPusHmOmQgKWPr'), orders=[UUID('cfbbad2d-bc77-474b-8934-b2438e2abb34'), UUID('f2a48ce4-30b4-46e0-b2d1-813be8e87e35')])
    """

The last option, you can ignore fields in your generated object:

::

    defaults = {
        'number': {
            '_ignore_': True
        }
    }

    baker.make(Address, _attr_defaults=defaults)

    """
    Address(number=None, street_name='YqgpvEISVKzAlfeemJil')
    """
