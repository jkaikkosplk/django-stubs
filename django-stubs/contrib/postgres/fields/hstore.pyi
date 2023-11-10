from typing import Any, ClassVar

from django.contrib.postgres.fields.array import ArrayField
from django.db.models import Field, TextField, Transform
from django.db.models.fields.mixins import CheckFieldDefaultMixin

class HStoreField(CheckFieldDefaultMixin, Field):
    def get_transform(self, name: str) -> Any: ...

class KeyTransform(Transform):
    output_field: ClassVar[TextField]

    def __init__(self, key_name: str, *args: Any, **kwargs: Any) -> None: ...

class KeyTransformFactory:
    def __init__(self, key_name: str) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> KeyTransform: ...

class KeysTransform(Transform):
    output_field: ClassVar[ArrayField]

class ValuesTransform(Transform):
    output_field: ClassVar[ArrayField]
