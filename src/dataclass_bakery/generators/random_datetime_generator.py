import random
from datetime import datetime, MAXYEAR, MINYEAR

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_generator import RandomGenerator


class RandomDatetimeGenerator(RandomGenerator):
    """
    Class to generate random date number
    """

    def generate(self, *args, **kwargs) -> datetime:
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

        min_hour_limit = kwargs.get(
            defaults.HOUR_MIN_LIMIT_ARG, defaults.HOUR_MIN_LIMIT
        )
        if min_hour_limit < 0:
            raise ValueError("Error: Min hour incorrect")

        max_hour_limit = kwargs.get(
            defaults.HOUR_MAX_LIMIT_ARG, defaults.HOUR_MAX_LIMIT
        )
        if max_hour_limit > 23:
            raise ValueError("Error: Max hour incorrect")

        if min_hour_limit > max_hour_limit:
            raise ValueError("Error: Min hour > Max hour")

        min_minute_limit = kwargs.get(
            defaults.MINUTE_MIN_LIMIT_ARG, defaults.MINUTE_MIN_LIMIT
        )
        if min_minute_limit < 0:
            raise ValueError("Error: Min minute incorrect")

        max_minute_limit = kwargs.get(
            defaults.MINUTE_MAX_LIMIT_ARG, defaults.MINUTE_MAX_LIMIT
        )
        if max_minute_limit > 59:
            raise ValueError("Error: Max minute incorrect")

        if min_minute_limit > max_minute_limit:
            raise ValueError("Error: Min minute > Max minute")

        min_second_limit = kwargs.get(
            defaults.SECOND_MIN_LIMIT_ARG, defaults.SECOND_MIN_LIMIT
        )
        if min_second_limit < 0:
            raise ValueError("Error: Min second incorrect")

        max_second_limit = kwargs.get(
            defaults.SECOND_MAX_LIMIT_ARG, defaults.SECOND_MAX_LIMIT
        )
        if max_second_limit > 59:
            raise ValueError("Error: Max second incorrect")

        if min_second_limit > max_second_limit:
            raise ValueError("Error: Min second > Max second")

        day = random.randint(min_day_limit, max_day_limit)
        month = random.randint(min_month_limit, max_month_limit)
        year = random.randint(min_year_limit, max_year_limit)
        hour = random.randint(min_hour_limit, max_hour_limit)
        month = random.randint(min_month_limit, max_month_limit)
        second = random.randint(min_second_limit, max_second_limit)

        new_datetime = datetime(year, month, day, hour, month, second)
        return new_datetime
