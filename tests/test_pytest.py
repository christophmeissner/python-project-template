import pytest
import logging

logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_xfails(hello):
    logger.debug(f"This comes from the fixture: {hello=}")
    pytest.xfail("failing xfail")


def test_passes(hello):
    assert hello == "hello"


def test_fails(hello):
    assert hello == "Hallo"
