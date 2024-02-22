import random
from datetime import date, MAXYEAR, MINYEAR

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_generator import RandomGenerator


class RandomDateGenerator(RandomGenerator):
    """
    Class to generate random date number
    """

    def generate(self, *args, **kwargs) -> date:
        min_day_limit = kwargs.get(defaults.DAY_MIN_LIMIT_ARG, defaults.DAY_MIN_LIMIT)
        if min_day_limit < 1:
            raise ValueError("Error: Min day incorrect")

        max_day_limit = kwargs.get(defaults.DAY_MAX_LIMIT_ARG, defaults.DAY_MAX_LIMIT)
        if max_day_limit > 28:
            raise ValueError("Error: Max day incorrect")

        min_month_limit = kwargs.get(
            defaults.MONTH_MIN_LIMIT_ARG, defaults.MONTH_MIN_LIMIT
        )
        if min_month_limit < 1:
            raise ValueError("Error: Min month incorrect")

        max_month_limit = kwargs.get(
            defaults.MONTH_MAX_LIMIT_ARG, defaults.MONTH_MAX_LIMIT
        )
        if max_month_limit > 12:
            raise ValueError("Error: Max month incorrect")

        if min_month_limit > max_month_limit:
            raise ValueError("Error: Min month > Max month")

        min_year_limit = kwargs.get(
            defaults.YEAR_MIN_LIMIT_ARG, defaults.YEAR_MIN_LIMIT
        )
        if min_year_limit < MINYEAR:
            raise ValueError("Error: Min year incorrect")

        max_year_limit = kwargs.get(
            defaults.YEAR_MAX_LIMIT_ARG, defaults.YEAR_MAX_LIMIT
        )
        if max_year_limit > MAXYEAR:
            raise ValueError("Error: Max year incorrect")

        if min_year_limit > max_year_limit:
            raise ValueError("Error: Min year > Max year")

        day = random.randint(min_day_limit, max_day_limit)
        month = random.randint(min_month_limit, max_month_limit)
        year = random.randint(min_year_limit, max_year_limit)

        new_date = date(year, month, day)
        return new_date
