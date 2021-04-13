# dataclass-bakery
Dataclass Bakery offers you a smart way to create fixtures for testing in Python with dataclasses

### Install

`pip install dataclass_bakery`

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

#### Types available:

 - int
 - str
 - float
 - bool
 - complex
 - range
 - list
 - tuple
 - dict
 - set
 - List (from typing import List)
 - Tuple (from typing import Tuple)
 - Dict (from typing import Dict)
 - Path (from pathlib import Path)
 - Decimal (from decimal import Decimal)


#### Next steps

 - Include more attr types
 - Feature to customize the random attributes (MAX_LENGHT, MIN_LIMIT, MAX_LIMIT...)
 - Feature to customize what generator use with what attribute
