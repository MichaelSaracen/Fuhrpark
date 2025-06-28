import pytest

from app.core import RegexValidator

@pytest.mark.parametrize("price,expected", [
    ("200", True),
    ("200.2", True),
    ("0.22", True),
    (".22", False),
    ("2.2.2", False),
])
def test_prices(price, expected):
    if expected:
        assert RegexValidator.prices(price)
    else:
        assert not RegexValidator.prices(price)
