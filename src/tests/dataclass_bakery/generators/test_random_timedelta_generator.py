from datetime import timedelta
from unittest import TestCase

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_timedelta_generator import (
    RandomTimedeltaGenerator,
)


class TestRandomTimedeltaGenerator(TestCase):
    def setUp(self):
        self.random_timedelta_generator = RandomTimedeltaGenerator()

    def test_generate_timedelta_ok(self):
        random_timedelta = self.random_timedelta_generator.generate()
        self.assertIsInstance(random_timedelta, timedelta)

    def test_generate_timedelta_incorrect_min_days_ko(self):
        min_days = -1
        with self.assertRaises(ValueError):
            self.random_timedelta_generator.generate(
                **{defaults.TIMEDELTA_DAYS_MIN_LIMIT_ARG: min_days}
            )

    def test_generate_timedelta_incorrect_days_range_ko(self):
        with self.assertRaises(ValueError):
            self.random_timedelta_generator.generate(
                **{
                    defaults.TIMEDELTA_DAYS_MIN_LIMIT_ARG: 10,
                    defaults.TIMEDELTA_DAYS_MAX_LIMIT_ARG: 5,
                }
            )
