Dataclass Bakery
================

Dataclass Bakery offers you a smart way to create objects based on dataclasses for testing in Python.
Inspired in model bakery module for Django.

Install
~~~~~~~

``pip install dataclass_bakery``

Usage and Info
~~~~~~~~~~~~~~

Basic usage
^^^^^^^^^^^

::

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

For more information: https://dataclass-bakery.readthedocs.io/

Types available:
^^^^^^^^^^^^^^^^

-  int
-  str
-  float
-  bool
-  complex
-  range
-  list
-  tuple
-  dict
-  set
-  List (from typing import List)
-  Tuple (from typing import Tuple)
-  Dict (from typing import Dict)
-  Union (from typing import Union)
-  Optional (from typing import Optional)
-  Path (from pathlib import Path)
-  Decimal (from decimal import Decimal)
-  UUID (from uuid import UUID)

