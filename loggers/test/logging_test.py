from my_logger import logging as sut
import pytest

class TestJSONLogger:
    @pytest.mark.custom
    def test_json_logger_custom_test(self, caplog):
        LOG = sut.get_json_logger(name="test-json-logger")
        LOG.setLevel(level="DEBUG")
        LOG.info("This is info")
        assert len(caplog.records) == 1
        assert caplog.records[0].levelname == "INFO"
        LOG.debug("This is debugging")
        assert len(caplog.records) == 2
        assert caplog.records[1].levelname == "DEBUG"

    def test_json_logger(self, caplog):
        LOG = sut.get_json_logger(name="test-json-logger")
        LOG.setLevel(level="DEBUG")
        LOG.info("This is info")
        assert len(caplog.records) == 1
        assert caplog.records[0].levelname == "INFO"
        LOG.debug("This is debugging")
        LOG.warning("This is a warning")
        LOG.error("This is an error")
        assert len(caplog.records) == 4
        assert caplog.records[1].levelname == "DEBUG"
        assert caplog.records[2].levelname == "WARNING"
        assert caplog.records[3].levelname == "ERROR"

