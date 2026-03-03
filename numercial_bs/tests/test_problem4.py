import pytest
from src.problem4 import Pipeline


class TestPipelineBasics:
    def test_empty_pipeline(self):
        p = Pipeline()
        assert p.execute(42) == 42

    def test_single_step(self):
        p = Pipeline()
        p.add_step("double", lambda x: x * 2)
        assert p.execute(5) == 10

    def test_multiple_steps_in_order(self):
        p = Pipeline()
        p.add_step("double", lambda x: x * 2)
        p.add_step("add_one", lambda x: x + 1)
        assert p.execute(5) == 11  # 5*2=10, 10+1=11

    def test_order_matters(self):
        p = Pipeline()
        p.add_step("add_one", lambda x: x + 1)
        p.add_step("double", lambda x: x * 2)
        assert p.execute(5) == 12  # 5+1=6, 6*2=12

    def test_steps_list(self):
        p = Pipeline()
        p.add_step("a", lambda x: x)
        p.add_step("b", lambda x: x)
        p.add_step("c", lambda x: x)
        assert p.steps() == ["a", "b", "c"]

    def test_empty_steps_list(self):
        p = Pipeline()
        assert p.steps() == []


class TestPipelineChaining:
    def test_add_step_returns_self(self):
        p = Pipeline()
        result = p.add_step("step1", lambda x: x)
        assert result is p

    def test_method_chaining(self):
        result = (
            Pipeline()
            .add_step("double", lambda x: x * 2)
            .add_step("add_one", lambda x: x + 1)
            .execute(5)
        )
        assert result == 11

    def test_remove_returns_self(self):
        p = Pipeline()
        p.add_step("step1", lambda x: x)
        result = p.remove_step("step1")
        assert result is p


class TestPipelineRemove:
    def test_remove_step(self):
        p = Pipeline()
        p.add_step("double", lambda x: x * 2)
        p.add_step("add_one", lambda x: x + 1)
        p.remove_step("double")
        assert p.execute(5) == 6  # only add_one runs
        assert p.steps() == ["add_one"]

    def test_remove_nonexistent_raises(self):
        p = Pipeline()
        with pytest.raises(KeyError):
            p.remove_step("nope")


class TestPipelineErrors:
    def test_duplicate_name_raises(self):
        p = Pipeline()
        p.add_step("step1", lambda x: x)
        with pytest.raises(ValueError):
            p.add_step("step1", lambda x: x * 2)


class TestPipelineWithDifferentTypes:
    def test_string_pipeline(self):
        result = (
            Pipeline()
            .add_step("upper", lambda s: s.upper())
            .add_step("exclaim", lambda s: s + "!")
            .execute("hello")
        )
        assert result == "HELLO!"

    def test_list_pipeline(self):
        result = (
            Pipeline()
            .add_step("sort", lambda lst: sorted(lst))
            .add_step("reverse", lambda lst: list(reversed(lst)))
            .execute([3, 1, 2])
        )
        assert result == [3, 2, 1]

    def test_type_changing_pipeline(self):
        """Steps can change the data type between stages."""
        result = (
            Pipeline()
            .add_step("to_str", lambda x: str(x))
            .add_step("length", lambda s: len(s))
            .execute(12345)
        )
        assert result == 5
