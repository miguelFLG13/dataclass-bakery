from datetime import date, MAXYEAR, MINYEAR
from unittest import TestCase

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_date_generator import RandomDateGenerator


class TestRandomDateGenerator(TestCase):
    def setUp(self):
        self.random_date_generator = RandomDateGenerator()

    def test_generate_date_ok(self):
        random_date = self.random_date_generator.generate()
        self.assertIsInstance(random_date, date)

    def test_generate_date_incorrect_min_day_ko(self):
        min_day = 0
        with self.assertRaises(ValueError):
            self.random_date_generator.generate(**{defaults.DAY_MIN_LIMIT_ARG: min_day})

    def test_generate_date_incorrect_max_day_ko(self):
        max_day = 32
        with self.assertRaises(ValueError):
            self.random_date_generator.generate(**{defaults.DAY_MAX_LIMIT_ARG: max_day})

    def test_generate_date_incorrect_min_month_ko(self):
        min_month = 0
        with self.assertRaises(ValueError):
            self.random_date_generator.generate(
                **{defaults.MONTH_MIN_LIMIT_ARG: min_month}
            )

    def test_generate_date_incorrect_max_month_ko(self):
        max_month = 13
        with self.assertRaises(ValueError):
            self.random_date_generator.generate(
                **{defaults.MONTH_MAX_LIMIT_ARG: max_month}
            )

    def test_generate_date_incorrect_min_year_ko(self):
        min_year = MINYEAR - 1
        with self.assertRaises(ValueError):
            self.random_date_generator.generate(
                **{defaults.YEAR_MIN_LIMIT_ARG: min_year}
            )

    def test_generate_date_incorrect_max_year_ko(self):
        max_year = MAXYEAR + 1
        with self.assertRaises(ValueError):
            self.random_date_generator.generate(
                **{defaults.YEAR_MAX_LIMIT_ARG: max_year}
            )
