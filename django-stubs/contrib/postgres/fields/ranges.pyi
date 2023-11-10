from typing import Any, ClassVar, Literal

from django.db import models
from django.db.models.lookups import PostgresOperatorLookup
from psycopg2.extras import DateRange, DateTimeTZRange, NumericRange, Range

class RangeBoundary(models.Expression):
    lower: str
    upper: str
    def __init__(self, inclusive_lower: bool = ..., inclusive_upper: bool = ...) -> None: ...

class RangeOperators:
    EQUAL: Literal["="]
    NOT_EQUAL: Literal["<>"]
    CONTAINS: Literal["@>"]
    CONTAINED_BY: Literal["<@"]
    OVERLAPS: Literal["&&"]
    FULLY_LT: Literal["<<"]
    FULLY_GT: Literal[">>"]
    NOT_LT: Literal["&>"]
    NOT_GT: Literal["&<"]
    ADJACENT_TO: Literal["-|-"]

class RangeField(models.Field):
    empty_strings_allowed: bool
    base_field: models.Field
    range_type: type[Range]
    def get_prep_value(self, value: Any) -> Any | None: ...
    def to_python(self, value: Any) -> Any: ...

class IntegerRangeField(RangeField):
    def __get__(self, instance: Any, owner: Any) -> NumericRange: ...

class BigIntegerRangeField(RangeField):
    def __get__(self, instance: Any, owner: Any) -> NumericRange: ...

class DecimalRangeField(RangeField):
    def __get__(self, instance: Any, owner: Any) -> NumericRange: ...

class DateTimeRangeField(RangeField):
    def __get__(self, instance: Any, owner: Any) -> DateTimeTZRange: ...

class DateRangeField(RangeField):
    def __get__(self, instance: Any, owner: Any) -> DateRange: ...

class DateTimeRangeContains(PostgresOperatorLookup): ...

class RangeContainedBy(PostgresOperatorLookup):
    type_mapping: dict[str, str]

class FullyLessThan(PostgresOperatorLookup): ...
class FullGreaterThan(PostgresOperatorLookup): ...
class NotLessThan(PostgresOperatorLookup): ...
class NotGreaterThan(PostgresOperatorLookup): ...
class AdjacentToLookup(PostgresOperatorLookup): ...

class RangeStartsWith(models.Transform):
    @property
    def output_field(self) -> models.Field: ...

class RangeEndsWith(models.Transform):
    @property
    def output_field(self) -> models.Field: ...

class IsEmpty(models.Transform):
    output_field: ClassVar[models.BooleanField]

class LowerInclusive(models.Transform):
    output_field: ClassVar[models.BooleanField]

class LowerInfinite(models.Transform):
    output_field: ClassVar[models.BooleanField]

class UpperInclusive(models.Transform):
    output_field: ClassVar[models.BooleanField]

class UpperInfinite(models.Transform):
    output_field: ClassVar[models.BooleanField]
