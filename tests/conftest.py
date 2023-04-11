import logging
import pytest

logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def hello():
    return "hello"
