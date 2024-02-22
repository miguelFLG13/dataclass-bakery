from datetime import datetime
from unittest import TestCase

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_datetime_generator import (
    RandomDatetimeGenerator,
)


class TestRandomDatetimeGenerator(TestCase):
    def setUp(self):
        self.random_datetime_generator = RandomDatetimeGenerator()

    def test_generate_datetime_ok(self):
        random_datetime = self.random_datetime_generator.generate()
        self.assertIsInstance(random_datetime, datetime)

    def test_generate_datetime_incorrect_min_hour_ko(self):
        min_hour = -1
        with self.assertRaises(ValueError):
            self.random_datetime_generator.generate(
                **{defaults.HOUR_MIN_LIMIT_ARG: min_hour}
            )

    def test_generate_datetime_incorrect_max_hour_ko(self):
        max_hour = 24
        with self.assertRaises(ValueError):
            self.random_datetime_generator.generate(
                **{defaults.HOUR_MAX_LIMIT_ARG: max_hour}
            )

    def test_generate_datetime_incorrect_min_minute_ko(self):
        min_minute = -1
        with self.assertRaises(ValueError):
            self.random_datetime_generator.generate(
                **{defaults.MINUTE_MIN_LIMIT_ARG: min_minute}
            )

    def test_generate_datetime_incorrect_max_minute_ko(self):
        max_minute = 61
        with self.assertRaises(ValueError):
            self.random_datetime_generator.generate(
                **{defaults.MINUTE_MAX_LIMIT_ARG: max_minute}
            )

    def test_generate_datetime_incorrect_min_second_ko(self):
        min_second = -1
        with self.assertRaises(ValueError):
            self.random_datetime_generator.generate(
                **{defaults.SECOND_MIN_LIMIT_ARG: min_second}
            )

    def test_generate_datetime_incorrect_max_second_ko(self):
        max_second = 61
        with self.assertRaises(ValueError):
            self.random_datetime_generator.generate(
                **{defaults.SECOND_MAX_LIMIT_ARG: max_second}
            )
