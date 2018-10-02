import pytest

@pytest.mark.parametrize("candidate,expected", [
    ('tachycardic', True),
])
def test_is_tachycardic(candidate, expected):
    from is_tachycardic import is_tachycardic
    assert is_tachycardic(candidate) == expected
