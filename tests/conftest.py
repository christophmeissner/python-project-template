import logging
import pytest

logger = logging.getLogger(__name__)


@pytest.fixture(scope="session")
def hallo():
    return "Hallo!"
