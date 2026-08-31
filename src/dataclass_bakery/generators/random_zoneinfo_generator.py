import random
from zoneinfo import ZoneInfo, available_timezones

from dataclass_bakery.generators.random_generator import RandomGenerator

AVAILABLE_TIMEZONES = sorted(available_timezones())


class RandomZoneinfoGenerator(RandomGenerator):
    """
    Class to generate a random IANA timezone (zoneinfo.ZoneInfo)
    """

    def generate(self, *args, **kwargs) -> ZoneInfo:
        timezone_name = random.choice(AVAILABLE_TIMEZONES)
        return ZoneInfo(timezone_name)
