import random
from datetime import timedelta

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_generator import RandomGenerator


class RandomTimedeltaGenerator(RandomGenerator):
    """
    Class to generate random timedelta
    """

    def generate(self, *args, **kwargs) -> timedelta:
        min_days_limit = kwargs.get(
            defaults.TIMEDELTA_DAYS_MIN_LIMIT_ARG, defaults.TIMEDELTA_DAYS_MIN_LIMIT
        )
        if min_days_limit < 0:
            raise ValueError("Error: Min days incorrect")

        max_days_limit = kwargs.get(
            defaults.TIMEDELTA_DAYS_MAX_LIMIT_ARG, defaults.TIMEDELTA_DAYS_MAX_LIMIT
        )
        if min_days_limit > max_days_limit:
            raise ValueError("Error: Min days > Max days")

        days = random.randint(min_days_limit, max_days_limit)
        seconds = random.randint(0, 86399)

        new_timedelta = timedelta(days=days, seconds=seconds)
        return new_timedelta
