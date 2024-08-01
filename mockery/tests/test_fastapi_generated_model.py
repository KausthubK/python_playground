from enum import Enum
from hypothesis import given, strategies as st
from pydantic import UUID4, BaseModel, conint, constr
from uuid import uuid4
import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from unittest.mock import MagicMock

from fast_api_generated_style_blah import Blah, BlahAPI, Status


@given(st.builds(Blah))
def test_blah(instance):
    assert isinstance(instance, Blah)


@given(
    st.builds(Blah, status=st.just(Status.ACTIVE)),
    st.builds(Blah, status=st.just(Status.INACTIVE)),
    st.builds(Blah, status=st.just(Status.DELETED)),
)
def test_status_of_blah(a, b, c):
    assert a.status == "active"
    assert b.status == "inactive"
    assert c.status == "deleted"


def test_the_real_blah():
    blah = BlahAPI(host="test.host.url")
    instance = blah.create_a_blah()
    assert isinstance(instance, Blah)
    assert len(str(instance.id)) == len("00000000-0000-0000-0000-000000000000")
    assert instance.status == "active"
    assert instance.additional_keys == []

@given(
    st.builds(Blah, status=st.just(Status.INACTIVE)),
)
def test_a_mock_blah(inactive_blah):
    blah_api = BlahAPI(host="test.host.url")
    assert blah_api.host == "test.host.url"
    blah_api.create_a_blah = MagicMock(return_value=inactive_blah)
    instance = blah_api.create_a_blah()
    assert isinstance(instance, Blah)
    assert len(str(instance.id)) == len("00000000-0000-0000-0000-000000000000")
    assert instance.status == "inactive"
    assert instance.additional_keys == []


@given(
    st.builds(BlahAPI),
    st.builds(Blah, status=st.just(Status.INACTIVE)),
)
def test_mocking_the_API(blah_api, inactive_blah):
    blah_api.create_a_blah = MagicMock(return_value=inactive_blah)
    b = blah_api.create_a_blah()
    assert isinstance(b, Blah)


def func_to_test(blah_api: BlahAPI) -> bool:
    blah = blah_api.create_a_blah()
    if blah.status == Status.ACTIVE:
        return True
    else:
        return False

@given(
    st.builds(BlahAPI),
    st.builds(Blah, status=st.just(Status.INACTIVE)),
)
def test_mocking_under_the_hood_usage(blah_api, inactive_blah):
    blah_api.create_a_blah = MagicMock(return_value=inactive_blah)
    retval = func_to_test(blah_api)
    assert retval == False

