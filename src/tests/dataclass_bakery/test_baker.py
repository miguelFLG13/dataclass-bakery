from unittest import TestCase
from unittest.mock import patch

from dataclass_bakery import baker
from tests.testing_dataclasses import Stuff


class TestBaker(TestCase):
    @patch(
        "dataclass_bakery.generators.random_data_class_generator.RandomDataClassGenerator.generate"
    )
    def test_baker_ok(self, mock_baker):
        quantity = 2
        mock_baker.return_value = Stuff(1)
        dataclass_objects = baker.make(Stuff, _quantity=quantity)
        self.assertEqual(len(dataclass_objects), quantity)

    def test_baker_incorrect_quantity(self):
        quantity = "asd"
        with self.assertRaises(TypeError):
            baker.make(Stuff, _quantity=quantity)

    def test_baker_incorrect_attr_defaults(self):
        attr_defaults = "asd"
        with self.assertRaises(TypeError):
            baker.make(Stuff, _attr_defaults=attr_defaults)
