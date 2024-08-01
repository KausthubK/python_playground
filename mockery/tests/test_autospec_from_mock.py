from enum import Enum
from pydantic import UUID4, BaseModel, conint, constr
from uuid import uuid4
import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from unittest.mock import MagicMock


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


def test_blah():
    instance = Blah(created_by="me", created_at=datetime.datetime.now(), archived=False, name="name", id=uuid4(), status=Status.ACTIVE, project_id=uuid4())
    assert isinstance(instance, Blah)


def test_status_of_blah():
    a = Blah(status=Status.ACTIVE, created_by="me", created_at=datetime.datetime.now(), archived=False, name="name", id=uuid4(), project_id=uuid4())
    assert a.status == "active"
    b = Blah(status=Status.INACTIVE, created_by="me", created_at=datetime.datetime.now(), archived=False, name="name", id=uuid4(), project_id=uuid4())
    assert b.status == "inactive"
    c = Blah(status=Status.DELETED, created_by="me", created_at=datetime.datetime.now(), archived=False, name="name", id=uuid4(), project_id=uuid4())
    assert c.status == "deleted"


def test_the_real_blah():
    blah = BlahAPI(host="test.host.url")
    instance = blah.create_a_blah()
    assert isinstance(instance, Blah)
    assert len(str(instance.id)) == len("00000000-0000-0000-0000-000000000000")
    assert instance.status == "active"
    assert instance.additional_keys == []


def test_a_mock_blah():
    inactive_blah = Blah(status=Status.INACTIVE, created_by="me", created_at=datetime.datetime.now(), archived=False, name="name", id=uuid4(), project_id=uuid4())
    blah_api = BlahAPI(host="test.host.url")
    assert blah_api.host == "test.host.url"
    blah_api.create_a_blah = MagicMock(return_value=inactive_blah)
    instance = blah_api.create_a_blah()
    assert isinstance(instance, Blah)
    assert len(str(instance.id)) == len("00000000-0000-0000-0000-000000000000")
    assert instance.status == "inactive"
    assert instance.additional_keys == []


def test_mocking_the_API():
    inactive_blah = Blah(status=Status.INACTIVE, created_by="me", created_at=datetime.datetime.now(), archived=False, name="name", id=uuid4(), project_id=uuid4())
    blah_api = BlahAPI(host="test.host.url")
    blah_api.create_a_blah = MagicMock(return_value=inactive_blah)
    b = blah_api.create_a_blah()
    assert isinstance(b, Blah)


def func_to_test(blah_api: BlahAPI) -> bool:
    blah = blah_api.create_a_blah()
    if blah.status == Status.ACTIVE:
        return True
    else:
        return False

def test_mocking_under_the_hood_usage():
    inactive_blah = Blah(status=Status.INACTIVE, created_by="me", created_at=datetime.datetime.now(), archived=False, name="name", id=uuid4(), project_id=uuid4())
    blah_api = BlahAPI(host="test.host.url")
    blah_api.create_a_blah = MagicMock(return_value=inactive_blah)
    retval = func_to_test(blah_api)
    assert retval == False

