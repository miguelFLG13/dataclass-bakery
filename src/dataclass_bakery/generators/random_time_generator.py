import random
from datetime import time

from dataclass_bakery.generators import defaults
from dataclass_bakery.generators.random_generator import RandomGenerator
from dataclass_bakery.generators.random_zoneinfo_generator import (
    RandomZoneinfoGenerator,
)


class RandomTimeGenerator(RandomGenerator):
    """
    Class to generate random time
    """

    def generate(self, *args, **kwargs) -> time:
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

        hour = random.randint(min_hour_limit, max_hour_limit)
        minute = random.randint(min_minute_limit, max_minute_limit)
        second = random.randint(min_second_limit, max_second_limit)

        tzinfo = None
        if kwargs.get(defaults.TZ_AWARE_ARG):
            tzinfo = RandomZoneinfoGenerator().generate()

        new_time = time(hour, minute, second, tzinfo=tzinfo)
        return new_time
