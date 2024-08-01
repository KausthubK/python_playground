from hypothesis import given, strategies as st
from pydantic import BaseModel, conint, constr


class User(BaseModel):
    age: conint(ge=1)
    first_name: constr(min_length=2)
    last_name: constr(min_length=2)


@given(st.builds(User))
def test_property(instance):
    assert isinstance(instance, User)
    assert instance.age > 0
    assert instance.last_name != ''

    