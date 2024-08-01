from hypothesis import given, strategies as st
from user import User

@given(st.builds(User))
def test_property(instance):
    assert isinstance(instance, User)
    assert instance.age > 0
    assert instance.last_name != ''

    