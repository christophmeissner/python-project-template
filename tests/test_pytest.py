import pytest
import logging

from main import HELLO, hello

logger = logging.getLogger(__name__)


@pytest.mark.xfail
def test_xfails(hello_fixture):
    logger.debug(f"This comes from the fixture: {hello_fixture=}")
    assert hello_fixture == hello()


def test_passes():
    assert hello() == HELLO
