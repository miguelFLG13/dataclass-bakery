from typing import Any, Dict, List, Optional, Union

from dataclass_bakery.generators.random_data_class_generator import (
    RandomDataClassGenerator,
)


def make(
    _data_class: Any,
    _quantity: Optional[int] = 1,
    _attr_defaults: Optional[Dict] = {},
) -> Union[List, Any]:
    random_data_class_generator = RandomDataClassGenerator()

    data_class_objects = []
    for _ in range(_quantity):
        data_class_object = random_data_class_generator.generate(
            _data_class, **_attr_defaults
        )
        data_class_objects.append(data_class_object)

    if _quantity > 1:
        return data_class_objects

    return data_class_object
