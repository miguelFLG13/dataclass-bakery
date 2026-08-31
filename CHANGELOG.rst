Changelog
=========

All notable changes to ``dataclass-bakery`` will be documented in this file.

The format is based on `Keep a Changelog <http://keepachangelog.com/>`__
and this project adheres to `Semantic
Versioning <http://semver.org/>`__.

`Unreleased <https://github.com/miguelFLG13/dataclass-bakery/tree/main>`__
---------------------------------------------------------------------------

Added
~~~~~

Changed
~~~~~~~

Removed
~~~~~~~

`1.0.0 <https://pypi.org/project/dataclass-bakery2/1.0.0/>`__
-------------------------------------------------------------

- **Important:** starting with this release, the PyPI distribution is published as ``dataclass-bakery2`` instead of ``dataclass-bakery`` (loss of access to the original PyPI account/project). The importable module is unchanged: ``import dataclass_bakery`` still works exactly the same. Install with ``pip install dataclass-bakery2``.

Added
~~~~~

- Add ``bytes``, ``bytearray``, ``frozenset``, ``time``, ``timedelta``, ``Fraction``, ``Enum``, ``IPv4Address``, ``IPv6Address``, ``deque``, ``OrderedDict``, ``Counter``, ``defaultdict``, ``Type``/``type`` and ``zoneinfo.ZoneInfo`` generators.
- Support ``Enum`` (and subclasses such as ``IntEnum``/``StrEnum``) as a dataclass attribute typing.
- Support ``typing.NamedTuple`` and ``typing.TypedDict`` classes as a dataclass attribute typing, generated the same way as a nested dataclass.
- Support **nested** generic typings inside any container generator, e.g. ``List[List[int]]`` or ``Dict[str, List[int]]``. Every container generator now resolves its item/key/value type the same way a top-level dataclass field is resolved (generic containers, ``Union``/``Optional``, ``Literal``, ``Enum``, nested dataclasses...).
- Add a ``_tz_aware_`` argument to the ``time``/``datetime`` generators to attach a random IANA timezone instead of a naive value.

Changed
~~~~~~~

- Replace the private ``typing._GenericAlias`` introspection in ``RandomDataClassGenerator`` with the public ``typing.get_origin``/``typing.get_args`` API. This fixes ``Union``/``Optional``/``Literal`` handling on Python 3.14 (where ``Union`` is no longer a ``_GenericAlias`` instance) and adds support for the PEP 604 ``X | Y`` syntax and the PEP 585 builtin generics (``list[int]``, ``dict[str, int]``, ...).
- ``Union[X, Y, Z]`` now picks a real random member among all the non-``None`` options on every call, instead of deterministically always resolving to the first declared type.
- Officially support and test against Python 3.12, 3.13 and 3.14.
- **Breaking:** raise the minimum supported Python version to 3.10 (``python_requires``); ``zoneinfo`` (3.9+) and ``typing.is_typeddict`` (3.10+) are used unconditionally at import time. The 3.7/3.8/3.9 classifiers were removed since they no longer reflected reality.
- Stop shipping the ``tests`` package as a top-level installable package (``setup.py`` now excludes it from ``find_packages``).
- Fix a ``setup.cfg`` parsing error (``[metadata]`` used the deprecated, incorrectly indented ``description-file`` key) that broke both a plain ``setuptools`` deprecation warning and ``pytest``'s own config discovery.

Fixed
~~~~~

- ``datetime`` generator: the ``minute`` component was never actually randomized — the ``month`` value was passed in its place, so ``_min_minute_limit_``/``_max_minute_limit_`` had no effect on the generated value.

Removed
~~~~~~~

`0.0.8 <https://pypi.org/project/dataclass-bakery/0.0.8/>`__
-------------------------------------------------------------

Added
~~~~~

- Add argument to ignore a field of a dataclass.

Changed
~~~~~~~

Removed
~~~~~~~

`0.0.7 <https://pypi.org/project/dataclass-bakery/0.0.7/>`__
-------------------------------------------------------------

Added
~~~~~

- Add datetime and date generators.

Changed
~~~~~~~

Removed
~~~~~~~

`0.0.6 <https://pypi.org/project/dataclass-bakery/0.0.6/>`__
-------------------------------------------------------------

Added
~~~~~

- Tests for all current generators.

Changed
~~~~~~~

- Improve generators to get dynamically the arguments to make an object. `PR #6 <https://github.com/miguelFLG13/dataclass-bakery/pull/6>`__
- Improve ``baker`` to get custom attributes of the objects. `PR #6 <https://github.com/miguelFLG13/dataclass-bakery/pull/6>`__

Removed
~~~~~~~


`0.0.5 <https://pypi.org/project/dataclass-bakery/0.0.5/>`__
------------------------------------------------------------

Added
~~~~~

- Add Literal Typing. `PR #4 <https://github.com/miguelFLG13/dataclass-bakery/pull/4>`__
- Add Options Generator. `PR #4 <https://github.com/miguelFLG13/dataclass-bakery/pull/4>`__

Changed
~~~~~~~

Removed
~~~~~~~

`0.0.3 <https://pypi.org/project/dataclass-bakery/0.0.3/>`__
------------------------------------------------------------

Added
~~~~~

- Add set generator. `PR #3 <https://github.com/miguelFLG13/dataclass-bakery/pull/3>`__
- Fix random data class generator to accept typing Optional and Union. `PR #3 <https://github.com/miguelFLG13/dataclass-bakery/pull/3>`__

Changed
~~~~~~~

Removed
~~~~~~~

`0.0.2 <https://pypi.org/project/dataclass-bakery/0.0.2/>`__
------------------------------------------------------------

Added
~~~~~


Changed
~~~~~~~

- Fix problems in random data class generator. `PR #2 <https://github.com/miguelFLG13/dataclass-bakery/pull/2>`__

Removed
~~~~~~~

`0.0.1 <https://pypi.org/project/dataclass-bakery/0.0.1/>`__
------------------------------------------------------------

Added
~~~~~

- Add first few generators. `PR #1 <https://github.com/miguelFLG13/dataclass-bakery/pull/1>`__
- Add baker. `PR #1 <https://github.com/miguelFLG13/dataclass-bakery/pull/1>`__

Changed
~~~~~~~

Removed
~~~~~~~
