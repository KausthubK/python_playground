from enum import Enum
from pydantic import UUID4
from uuid import uuid4
import datetime
from typing import Any, Dict, List, TypeVar

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


class BlahAPI():
    def __init__(self, host: str,):
        self.host = host

    def create_a_blah(self) -> Blah:
        return Blah(
            created_by="me",
            created_at=datetime.datetime.now(),
            archived=False,
            name="name",
            id=uuid4(),
            status=Status.ACTIVE,
            project_id=uuid4(),
        )