from enum import Enum
from hypothesis import given, strategies as st
from pydantic import UUID4, BaseModel, conint, constr

import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field


class Status(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    DELETED = "deleted"


T = TypeVar("T", bound="Blah")

@_attrs_define
class Blah:
    created_by: str
    created_at: datetime.datetime
    archived: bool
    name: str
    id: UUID4
    status: Status
    project_id: UUID4
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties


@given(st.builds(Blah))
def test_blah(instance):
    assert isinstance(instance, Blah)
    # assert instance.id == '00000000-0000-0000-0000-000000000000'
