class TypeNotAllow(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__("TypeNotAllow: Creating a dataclass object")
