Basic Usage
===========

Dataclass bakery basically generates an object based on a dataclass in a simple way, for example:

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

If you want to use dataclass bakery in a test, you can do it this way:

File: **customer.py** ::

    from dataclasses import dataclass


    class Customer:
        """
        Represent a Customer of our system
        """
        id: int
        name: str
        spent_money: Decimal
        avatar: Path

To create your tests using concrete objects created by dataclass bakery:

File: **test_customer_action.py** ::

    from unittest import TestCase

    from dataclass_bakery import baker

    from customer import Customer


    class CustomerActionTest(TestCase):
        """
        Class to test some action of a Customer
        """

        def setUp(self):
            self.customer = baker.make(Customer)

        ...
